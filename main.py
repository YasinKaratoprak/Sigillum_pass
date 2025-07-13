import sys
import os
import getpass

from core.manager import Manager
from core.storage import Storage
from utils.generator import Generator


def main():
    """Entry point for the CLI password manager."""
    password_file = "password.txt"
    if not os.path.exists(password_file):
        while True:
            new_password = getpass.getpass("Set a new program password: ")
            confirm_password = getpass.getpass("Confirm password: ")
            if new_password == confirm_password and new_password.strip():
                with open(password_file, "w") as f:
                    f.write(new_password)
                print("Password set successfully.")
                break
            else:
                print("Passwords do not match or empty. Try again.")
    else:
        while True:
            entered = getpass.getpass("Enter your program password: ")
            with open(password_file, "r") as f:
                saved = f.read().strip()
            if entered == saved:
                print("Access granted.")
                break
            else:
                print("Incorrect password. Try again.")

    storage = Storage()
    manager = Manager()
    generator = Generator()

    # Load accounts from file
    accounts = storage.load_accounts()
    manager.load_accounts(accounts)

    password_view_unlocked = False

    while True:
        print(
            "\n1. Add Account\n2. List Accounts\n3. Remove Account\n4. Generate Password\n"
            "5. Password Update\n6. Password Strength Health\n7. Show Passwords\n"
            "8. Update Program Password\n9. Exit"
        )
        choice = input("Select an option: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = getpass.getpass("Password (leave empty to generate): ")
            if not password:
                print(
                    "Password options:\n1. Letters, digits, special\n2. Letters, digits\n"
                    "3. Letters only\n4. Digits only"
                )
                opt = input("Select option: ")
                length = int(input("Password length: "))
                if opt == "1":
                    password = generator.option1(length)
                elif opt == "2":
                    password = generator.option2(length)
                elif opt == "3":
                    password = generator.option3(length)
                elif opt == "4":
                    password = generator.option4(length)
                else:
                    print("Invalid option.")
                    continue
                print(f"Generated password: {password}")
            account = {"site": site, "username": username, "password": password}
            added = manager.add_account(account)
            if added:
                storage.save_accounts(manager.account)

        elif choice == "2":
            if not password_view_unlocked:
                check = getpass.getpass(
                    "Enter your program password to list accounts: "
                )
                with open(password_file, "r") as f:
                    saved = f.read().strip()
                if check != saved:
                    print("Incorrect password. Access denied.")
                    continue
                password_view_unlocked = True
            manager.list_account()

        elif choice == "3":
            removeAll = input("Remove all accounts? (y/n): ")
            if removeAll == "y":
                manager.account.clear()
                storage.save_accounts(manager.account)
                print("All accounts removed.")
                continue
            elif removeAll == "n":
                site = input("Site: ")
                username = input("Username: ")
                to_remove = None
                for acc in manager.account:
                    if acc.get("site") == site and acc.get("username") == username:
                        to_remove = acc
                        break
                if to_remove:
                    manager.remove_account(to_remove)
                    storage.save_accounts(manager.account)
                    print("Account removed.")
                else:
                    print("Account not found.")

        elif choice == "4":
            print(
                "Password options:\n1. Letters, digits, special\n2. Letters, digits\n"
                "3. Letters only\n4. Digits only"
            )
            opt = input("Select option: ")
            length = int(input("Password length: "))
            if opt == "1":
                print(generator.option1(length))
            elif opt == "2":
                print(generator.option2(length))
            elif opt == "3":
                print(generator.option3(length))
            elif opt == "4":
                print(generator.option4(length))
            else:
                print("Invalid option.")

        elif choice == "5":
            site = input("Site: ")
            username = input("Username: ")
            new_password = getpass.getpass("New Password: ")
            manager.password_update(site, username, new_password)
            storage.save_accounts(manager.account)

        elif choice == "6":
            print("Password Strength Health:")
            for account in manager.account:
                site = account.get("site")
                username = account.get("username")
                password = account.get("password")
                if password:
                    strength = generator.check_password_strength(password)
                    print(
                        f"Site: {site}, Username: {username}, Password Strength: {strength}"
                    )
                else:
                    print(f"Site: {site}, Username: {username}, Password: Not set")

        elif choice == "7":
            if not password_view_unlocked:
                check = getpass.getpass(
                    "Enter your program password to view passwords: "
                )
                with open(password_file, "r") as f:
                    saved = f.read().strip()
                if check != saved:
                    print("Incorrect password. Access denied.")
                    continue
                password_view_unlocked = True
            print("All account passwords:")
            for account in manager.account:
                print(
                    f"Site: {account.get('site')}, Username: {account.get('username')}, Password: {account.get('password')}"
                )

        elif choice == "8":
            with open(password_file, "r") as f:
                saved = f.read().strip()
            old = getpass.getpass("Enter your current program password: ")
            if old != saved:
                print("Incorrect password. Password not changed.")
                continue
            while True:
                new_password = getpass.getpass("Enter new program password: ")
                confirm_password = getpass.getpass("Confirm new password: ")
                if new_password == confirm_password and new_password.strip():
                    with open(password_file, "w") as f:
                        f.write(new_password)
                    print("Program password updated successfully.")
                    password_view_unlocked = False
                    break
                else:
                    print("Passwords do not match or empty. Try again.")

        elif choice == "9":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

