import random
import string

class Robot:
    def _gen_name(self):
        random.seed()
        return "".join(random.sample(string.ascii_uppercase, 2) + random.sample(string.digits, 3))
    def __init__(self):
        self.name = self._gen_name()
    def reset(self):
        self.name = self._gen_name()
        
        
