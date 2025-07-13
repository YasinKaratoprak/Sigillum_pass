# Password Manager

A simple CLI-based password manager written in Python.

## Features

- Add Account
  - Site
  - Username
  - Password (manual or generated)
- List Accounts (password-protected)
- Remove Account (single or all)
- Password Generator
  - Custom length
  - Character set options:
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters
- Update Account Password
- Password Strength Health Check
- Show All Passwords (password-protected)
- Update Program Password

## Usage

1. **Install Python 3.7+**
2. **Clone the repository**
3. **Run the application**: `python3 main.py`
4. **Follow the CLI menu to manage your accounts and generate passwords.**

## File Structure

- `main.py` - Main CLI application and menu
- `core/manager.py` - Account management logic (add, remove, update, list)
- `core/storage.py` - Save/load accounts to/from `data.password.json`
- `utils/generator.py` - Password generation and strength checking utilities
- `data.password.json` - Stores all account data in JSON format
- `password.txt` - Stores the program's master password

## Data Storage

All account data is stored in `data.password.json` in JSON format. The program password is stored in `password.txt` (plain text).

## Security Note

- The program password is required to view or list passwords and accounts.
- Passwords are stored in plain text for simplicity. For real-world use, consider encrypting stored data or using a dedicated secrets manager.
- The repository's `.gitignore` excludes `password.txt` and `data.password.json` to avoid leaking sensitive information.

## License

MIT License

