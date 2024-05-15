import random
import string

class RandomValueGenerator:

    @classmethod
    def random_generator(cls,size=8, chars=string.ascii_lowercase + string.digits+string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(size))
