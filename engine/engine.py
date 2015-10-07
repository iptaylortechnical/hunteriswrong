__author__ = 'Isaiah'

class engine:

    def __init__(self, users, games, slots):
        if not users % slots == 0:
            raise ValueError("users and slots not divisible")