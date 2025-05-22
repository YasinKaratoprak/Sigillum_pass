# Password Manager

A simple CLI-based password manager written in Python.

## Features

- Add Account
  - Site
  - Username
  - Password (manual or generated)
- List Accounts
- Remove Account
- Password Generator
  - Custom length
  - Character set options:
    - Uppercase letters
    - Lowercase letters
    - Digits
    - Special characters

## Usage

1. **Install Python 3.7+**
2. **Clone the repository**
3. **Run the application** => python3 main.py
4. **Follow the CLI menu to manage your accounts and generate passwords.**

## File Structure

- `main.py` - Main CLI application
- `core/manager.py` - Account management logic
- `core/storage.py` - Save/load accounts to/from `data.password.json`
- `utils/generator.py` - Password generation utilities

## Data Storage

All account data is stored in `data.password.json` in JSON format.

## License

MIT License