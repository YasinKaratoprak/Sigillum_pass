import random
import string


class Generator:
    """Password generation and evaluation utilities."""

    def __init__(self):
        pass

    def option1(self, length: int) -> str:
        """Letters, digits and special characters."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def option2(self, length: int) -> str:
        """Letters and digits."""
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def option3(self, length: int) -> str:
        """Letters only."""
        characters = string.ascii_letters
        return ''.join(random.choice(characters) for _ in range(length))

    def option4(self, length: int) -> str:
        """Digits only."""
        characters = string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def check_password_strength(self, password: str) -> str:
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
        return "Strong"
