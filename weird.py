import copy
import random

from flask import render_template

import colour
import dice


class WierdGenerator(object):

    WEIRD = open('weird.txt').read().split('\n')

    def __init__(self):
        self.init_weird()

    def init_weird(self):
        self._weird = copy.copy(WierdGenerator.WEIRD)
        random.shuffle(self._weird)

    def weird(self):
        if not self._weird:
            return self.init_weird()
        entry = self._weird.pop().format(colour=colour.colour(),
                    hex="%02d%02d" % (dice.d(26), dice.d(16)))
        return Weird(entry)


class Weird(object):
    """
    Most of the hexes in Carcosa are weird-ass stuff.
    """
    def __init__(self, weird):
        self.description = render_template("weird_description.html", weird=weird)
