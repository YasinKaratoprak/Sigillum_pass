
class Manager:
    def __init__(self):
        self.account = []

    def add_account(self, account):
        self.account.append(account)

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
