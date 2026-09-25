import random
import string

class Helper:
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))