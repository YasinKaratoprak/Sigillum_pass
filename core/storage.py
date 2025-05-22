import json
import os

class Storage:
    def __init__(self, filepath='data.password.json'):
        self.filepath = filepath

    def save_accounts(self, accounts):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)

    def load_accounts(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []