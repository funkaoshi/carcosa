import random
from flask import render_template

import colour
from dice import d, xdy


class Settlement(object):
    """
    Generate a random Carcosa themed settlement.
        * There are 800 keyed encounters in Carcosa.
        * 233ish of them describe villages, citadels, castles or monasteries.
        * Monastery: 4 (1-2), Castle: 41 (3-20), Village: 138,
          Citadel: 50 (21-42), Village (42-100)
        * Race: 2% chance for mutated race, otherwise even distribution.
          (More or less.)
        * Almost all villages are "ruled" by someone, all castles/citadels
          are "led" by someone. (Looking into this more carefully, it looks
          like Castles / Citadels are "led", villages are "ruled".
        * There is a 1% chance the settlement is leaderless.
    """

    def __init__(self):
        self.kind = self.get_kind()
        self.colour = self.get_colour()
        self.population = self.get_population(self.kind)
        self.leader = self.get_leader(self)

    @property
    def description(self):
        return render_template("settlement_description.html", settlement=self)

    def get_kind(self):
        roll = d(100)
        if roll <= 2:
            return "Monastery"
        elif roll <= 20:
            return "Castle"
        elif roll <= 42:
            return "Citadel"
        else:
            return "Village"

    def get_colour(self):
        roll = d(100)
        if roll <= 2:
            return "Mutated"
        return colour.colour()

    def get_population(self, kind):
        # TODO: Figure out actual distribution. These are pretty close.
        if kind == 'Village':
            return xdy(5,95) + 25
        elif kind == 'Castle':
            return xdy(2,50)
        elif kind == 'Citadel':
            return d(100) + d(50)
        else:
            return xdy(5,16) + d(10) + 10

    def get_leader(self, kind):
        roll = d(100)
        if roll <= 2:
            return None
        return Leader(kind)


class Leader(object):
    """
    Describes a leader of a settlement in Carcosa.
        * Leader's Alignment: Chaotic (1-29), Neutral (30-81), Lawful (82-100)
        * Class: Fighter (1-77), Sorcerer (77-99), Spawn of Shub-Niggurath (100)
            * Flip stats for Fighter and Sorcerer when dealing with a monastery.
    """

    def read_file(filename):
        """
        Reads a list of names. Ignore the last empty entry.
        """
        return open(filename).read().split('\n')

    NOUNS = read_file('names_nouns.txt')
    ADJECTIVES = read_file('names_adjectives.txt')
    DESCRIPTIONS = read_file('names_descriptions.txt')

    def __init__(self, settlement):
        self.character_class = self.get_class(settlement.kind)
        self.alignment = self.get_alignment()
        self.level = self.get_level()
        self.name = self.get_name(settlement.colour)

    def get_class(self, kind):
        roll = d(100)
        if roll == 100:
            return "Spawn of Shub-Niggurath"
        if roll <= 77:
            return "Fighter" if kind != "Monastery" else "Sorcerer"
        else:
            return "Sorcerer" if kind != "Monastery" else "Fighter"

    def get_alignment(self):
        roll = d(100)
        if roll <= 29:
            return "Chaotic"
        elif roll <= 81:
            return "Neutral"
        else:
            return "Lawful"

    def get_level(self):
        roll = d(100)
        if roll <= 1:
            return "1st"
        elif roll <= 5:
            return "2nd"
        elif roll <= 13:
            return "3rd"
        elif roll <= 26:
            return "4th"
        elif roll <= 42:
            return "5th"
        elif roll <= 58:
            return "6th"
        elif roll <= 73:
            return "7th"
        elif roll <= 83:
            return "8th"
        elif roll <= 91:
            return "9th"
        elif roll <= 96:
            return "10th"
        elif roll <= 99:
            return "11th"
        else:
            return random.choice(["12th", "12th", "12th", "13th", "13th",
                                 "14th", "15th", "16th"])

    def get_name(self, colour):
        roll = d(100)
        if roll > 65:
            return None

        adjective = random.choice(Leader.ADJECTIVES)
        noun = random.choice(Leader.NOUNS)
        description = random.choice(Leader.DESCRIPTIONS)

        used_adjective = False
        try:
            description = description.format(adjective=adjective)
            used_adjective = True
        except KeyError:
            pass
        try:
            description = description.format(colour=colour)
        except KeyError:
            pass

        roll = d(12)
        if roll <= 3:
            name = [adjective, noun]
        elif roll <= 7:
            if not used_adjective:
                name = [adjective, noun, description]
            else:
                name = [noun, description]
        else:
            name = [noun, description]
        if not name[0] in ['He', 'Her', 'It', 'She', 'Lady']:
            name = ['the'] + name
        return ' '. join(name)

