import random

class Weird(object):
    """
    Most of the hexes in Carcosa are weird-ass stuff.
    """

    WEIRD = open('weird.txt').read().split('\n')

    def __init__(self):
        self.description = random.choice(Weird.WEIRD)

