import collections
import random

from flask import render_template

import colour
from dice import d, xdy

class Dinosaur(object):
    """
    Generate a mutant dinosaur, which are discussed in Carcosa, but not fleshed
    out enough to help DMs make their own easily.
    """

    #
    # TODO: Clean this all up.
    #

    def __init__(self):
        self.name = random.choice(Dinosaur.DINOSAURS_NAMES)
        self.dinosaur = Dinosaur.DINOSAURS[self.name]
        self.hd = self.dinosaur['HD']
        self.hd = random.randint(max(1, self.hd - 4), self.hd + 4)
        self.ac = self.dinosaur['AC']
        self.move = self.dinosaur['MV']
        self.colour = colour.colour()
        self.hide = random.choice(Dinosaur.HIDES)
        if 'attacks' in self.dinosaur:
            self.attacks = "%s attacks" % self.dinosaur['attacks']
        self.alignment = 'neutral'
        self.number = self.dinosaur['number']()
        self._get_features()
        self.powers = self._get_powers()
        self.immunities = self._get_immunities()

    DINOSAURS = {
        'Ankylosaurus': {
            'AC': 21,
            'MV': "60'",
            'HD': 9,
            'number': lambda: d(4) + 1,
        },
        'Allosaurus': {
            'AC': 16,
            'MV': "150'",
            'HD': 15,
            'number': lambda: d(2),
            'attacks': 3,
        },
        'Archelon lschyras': {
            'AC': 18,
            'MV': "30' [150' Swim]",
            'HD': 7,
            'number': lambda: d(4),
        },
        'Brachiosaurus': {
            'AC': 16,
            'MV': "60'",
            'HD': 36,
            'number': lambda: d(6),
        },
        'Brontosaurus': {
            'AC': 16,
            'MV': "60'",
            'HD': 30,
            'number': lambda: d(6),
        },
        'Camarasaurus': {
            'AC': 15,
            'MV': "60'",
            'HD': 12,
            'number': lambda: xdy(2, 4),
        },
        'Ceratosaurus': {
            'AC': 16,
            'MV': "150'",
            'HD': 8,
            'number': lambda: d(4),
            'attacks': 3,
        },
        'Gorgosaurus': {
            'AC': 16,
            'MV': "150'",
            'HD': 13,
            'number': lambda: d(2),
            'attacks': 3,
        },
        'Iguanadon': {
            'AC': 16,
            'MV': "150'",
            'HD': 6,
            'number': lambda: xdy(3, 6),
            'attacks': 3,
        },
        'Lambeosaurus': {
            'AC': 15,
            'MV': "120'",
            'HD': 12,
            'number': lambda: xdy(2, 8),
        },
        'Megalosaurus': {
            'AC': 16,
            'MV': "120'",
            'HD': 12,
            'number': lambda: d(2),
        },
        'Monoclonius': {
            'AC': 17,
            'MV': "60'",
            'HD': 8,
            'number': lambda: xdy(2, 6),
        },
        'Mosasaurus': {
            'AC': 14,
            'MV': "30' [150' Swim]",
            'HD': 12,
            'number': lambda: d(3),
        },
        'Paleoscincus': {
            'AC': 24,
            'HD': 9,
            'MV': "30'",
            'number': lambda: d(4),
        },
        'Pentaceratops': {
            'AC': 15,
            'HD': 12,
            'MV': "90'",
            'number': lambda: xdy(2, 6),
        },
        'Plateosaurus': {
            'AC': 16,
            'HD': 8,
            'MV': "80'",
            'number': lambda: xdy(5, 4),
        },
        'Plesiosaurus': {
            'AC': 14,
            'HD': 20,
            'MV': "150'",
            'number': lambda: d(3),
        },
        'Pteranodon': {
            'AC': 14,
            'HD': 4,
            'MV': "30' [150' Fly]",
            'number': lambda: xdy(3, 6),
        },
        'Stegosaurus': {
            'AC': 16,
            'HD': 8,
            'MV': "60'",
            'number': lambda: xdy(2, 8),
        },
        'Styracosaurus': {
            'AC': 17,
            'HD': 10,
            'MV': "60'",
            'number': lambda: xdy(2, 8),
        },
        'Teratosaurus': {
            'AC': 16,
            'HD': 10,
            'MV': "180'",
            'number': lambda: d(3),
        },
        'Trachodon': {
            'AC': 16,
            'MV': "120'",
            'HD': 12,
            'number': lambda: xdy(2, 6),
        },
        'Triceratops': {
            'AC': 15,
            'HD': 16,
            'MV': "90'",
            'number': lambda: xdy(2, 4),
        },
        'Tyrannosaurus Rex': {
            'AC': 16,
            'HD': 18,
            'MV': "150'",
            'number': lambda: d(2),
        },
        'Velociraptor': {
            'AC': 14,
            'HD': 2,
            'MV': "180'",
            'number': lambda: xdy(2, 4),
        }
    }

    DINOSAURS_NAMES = [name for name in list(DINOSAURS.keys())]

    DINOSAURS_BY_HD = collections.defaultdict(list)
    for name, dino in list(DINOSAURS.items()):
        DINOSAURS_BY_HD[dino['HD']].append(name)

    @property
    def description(self):
        return render_template("dinosaur_description.html", dinosaur=self)

    @property
    def monster_description(self):
        desc = []
        if self.eyes != 2:
            desc.append('%s eyes, ' % self.eyes.capitalize())
        desc.append('%s' % self.mouth)
        if d(10) > 5:
            desc.append(', ')
            desc.append(random.choice(Dinosaur.BODY_FEATURES))
        desc = ''.join(desc)
        if desc.strip():
            desc = desc + '.'
        return desc

    def _get_features(self):
        roll = d(10)
        if roll > 7:
            self.eyes = d(8) - 1
            if self.eyes == 0:
                self.eyes = 'no'
            elif self.eyes == 7:
                self.eyes = 'multiple/insectile'
        elif roll > 4:
            self.eyes = 'glowing',
        else:
            self.eyes = 2

        if d(10) > 7:
            self.mouth = random.choice(Dinosaur.MOUTHS)
            if self.eyes == 2:
                self.mouth = self.mouth.capitalize()

    def _get_powers(self):
        roll = d(100)
        if roll <= 25:
            return []
        if roll == 100:
            return random.sample(Dinosaur.POWERS, 2)
        else:
            return [random.choice(Dinosaur.POWERS)]

    def _get_immunities(self):
        roll = d(20)
        if roll <= 10:
            return []
        elif roll == 20:
            return random.sample(Dinosaur.IMMUNITIES, 2)
        else:
            return [random.choice(Dinosaur.IMMUNITIES)]

    HIDES = ['Smooth', 'Suckered', 'Scaled', 'Scaled', 'Feathered', 'Feathered', 'Furred']

    MOUTHS = ['no mouth', 'multiple mouths', 'beaked mouth', 'suckered mouth',
              'circular gaping maw', 'prehensile tongue (swallow attack)']

    BODY_FEATURES = [
        "metal body",
        "tentacles instead of legs",
        "2-9 heads",
    ]

    POWERS = [
        "Can cast invisibility at will.  When visible, has see-through skin like a Bone Man.",
        "Covered in spines (when attacked in melee attacker takes a dCarcosa damage and it can throw them like a wyvern).",
        "Pillow-like consistency, immune to bludgeoning attacks.",
        "Shoots eggs from its butt.",
        "Can split into smaller versions of itself, like Voltron in reverse.",
        "Immortal.  Will resurrect 1 minute after apparent death.",
        "Laser Eyes",
        "Genius Intelligence (18+ Int) and 1-4 psychic powers.",
        "Semi-gelatinous (suffer only half damage from weapons that are not electromagnetic or elemental).",
        "Tentacles for tongues (can grab prey up to 20' away).",
        "Breath weapon.",
        "Eyes glow brightly (Gaze causes confusion).",
        "Extremely cold (1 die damage per round to all within 20').",
        "Extremely hot (1 die damage per round to all within 20').",
        "Poisonous.",
        "Touch causes sickness (lose 1 Con / day until dead).",
        "Touch turns anyone to slime.",
        "Posses an additional 3 senses (Surprises on 1-4 on a d6).",
        "Psionic: (1-8 powers, 1-8 times per day).",
        "Can shoot tail spikes up to 60'.",
        "Poisoned tail spikes has the effect of green lotus powder.",
        "Radioactive (if killed explodes for 2 dice radiation damage to all within 100').",
    ]

    IMMUNITIES = [
        'Immune to normal weapons.',
        'Immune to cold.',
        'Surprised only on a 1.',
        'Invisible.',
        'Immune to poison.',
        'Immune to heat/fire.',
        'Immune to surprise.',
        'Regenerate 1 HD every 1-3 rounds.',
        'Harmed only by fire.',
    ]
