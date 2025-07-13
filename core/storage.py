import json
import os

class Storage:
    """Handle saving and loading account data from disk."""

    def __init__(self, filepath: str = "data.password.json"):
        self.filepath = filepath

    def save_accounts(self, accounts):
        """Persist accounts to disk in JSON format."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)

    def load_accounts(self):
        """Load accounts from disk, returning an empty list if none found."""
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

