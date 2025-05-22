
class Manager:
    def __init__(self):
        self.account = []

    def load_accounts(self, accounts):
        self.account = accounts
        if accounts:
            self.last_id = max(acc.get("id", 0) for acc in accounts)
        else:
            self.last_id = 0

    def add_account(self, account):
        # Check for duplicate
        for acc in self.account:
            if acc.get("site") == account.get("site") and acc.get("username") == account.get("username"):
                print("Account with this site and username already exists.")
                return False
        self.last_id += 1
        account["id"] = self.last_id
        self.account.append(account)
        print("Account added.")
        return True

    def remove_account(self, account):
        if account in self.account:
            self.account.remove(account)
        else:
            print("Account not found. Are you sure you added it?")

    def list_account(self):
        if not self.account:
            print("No accounts found.")
        else:
            for account in self.account:
                print(account)

    def password_update(self, site, username, new_password):
        for account in self.account:
            if account.get("site") == site and account.get("username") == username:
                account["password"] = new_password
                print(f"Password for {site} updated successfully.")
                return
        print("Account not found. Are you sure you added it?")



