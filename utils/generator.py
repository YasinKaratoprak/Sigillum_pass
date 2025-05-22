import random
import string

class Generator:
    def __init(self):
        self.account = []

    def option1(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def option2(self, length):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def option3(self, length):
        characters = string.ascii_letters
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def option4(self, length):
        characters = string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def check_password_strength(self, password):
        length = len(password)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
        score = 0
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if has_lower:
            score += 1
        if has_upper:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1
        if score <= 2:
            return "Weak"
        elif score <= 4:
            return "Moderate"
        else:
            return "Strong"

