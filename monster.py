import random
from flask import render_template

from dice import xdy

class Monster(object):
    """
    Generates a simple random monster encounter. About 12% of the hex
    descriptions in Carcosa are simple random monster encounters. (1 Dolm Ooze,
    12 Irrational Space Aliens, etc.)
    """

    # TODO: Load from file or table
    MONSTERS = [
        # rare
        (1, 3, "B'yakhee", "B'yakhees"),
        (1, 3, "Cthugah's Flame Creature", "Cthugah's Flame Creatures"),
        (1, 12, "of the Great Race", "of the Great Race"),
        (3, 4, "Mi-Go", "Mi-Go"),
        (1, 1, "Mummy Brain", "Mummy Brain"),
        (1, 10, "Primordial One", "Primordial Ones"),
        (1, 3, "Shoggoth", "Shoggoths"),
        (1, 100, "solitary Space Alien", "Space Aliens"),
        (1, 6, "individual of Species 23750", "individuals of Species 23750"),
        (1, 1, "Spawn of Yog-Sothoth", "Spawn of Yog-Sothoth"),
        (1, 4, "Unquiet Worm", "Unquiet Worms"),
        (6, 6, "Diseased Guardian", "Diseased Guardians"),
        (1, 6, "Pterodactyl", "Pterodactyls"), 
        (2, 8, "Stegosaurs", "Stegosauruses"),
        (3, 4, "Triceratops", "Triceratops"),
        (1, 2, "Tyrannosaurus Rex", "Tyrannosaurus Rexes"),
        (2, 6, "Velociraptor", "Velociraptors"),

        # common
        (1, 1, "Dolm Ooze", "Dolm Ooze"),
        (1, 1, "Dolm Pudding", "Dolm Pudding"),
        (1, 3, "Dolm Worm", "Dolm Worms"),
        (1, 12, "Mummy", "Mummies"),
        (1, 1, "Ulfire Jelly", "Ulfire Jelly"),
    ]

    def __init__(self):
        self.count, self.monster = self.get_monster()

    @property
    def description(self):
        return render_template("monster_description.html", monster=self)

    def get_monster(self):
        numdie, dietype, monster, monsters = random.choice(Monster.MONSTERS)
        count = xdy(numdie, dietype)
        if count > 1:
            monster = monsters
        return count, monster
