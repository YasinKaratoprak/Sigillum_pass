import sys
from core.manager import Manager
from core.storage import Storage
from utils.generator import Generator

def main():
    storage = Storage()
    manager = Manager()
    generator = Generator()

    # Load accounts from file
    manager.account = storage.load_accounts()

    while True:
        print("\n1. Add Account\n2. List Accounts\n3. Remove Account\n4. Generate Password\n5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            site = input("Site: ")
            username = input("Username: ")
            password = input("Password (leave empty to generate): ")
            if not password:
                print("Password options:\n1. Letters, digits, special\n2. Letters, digits\n3. Letters only\n4. Digits only")
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
            manager.add_account(account)
            storage.save_accounts(manager.account)
            print("Account added.")

        elif choice == "2":
            manager.list_account()

        elif choice == "3":
            site = input("Site: ")
            username = input("Username: ")
            # Find account to remove
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
            print("Password options:\n1. Letters, digits, special\n2. Letters, digits\n3. Letters only\n4. Digits only")
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
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()