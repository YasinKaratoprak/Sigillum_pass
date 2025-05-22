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