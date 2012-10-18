import random
from dice import d, xdy

class Spawn(object):
    def __init__(self):
        self.unique = d(20) != 20
        if not self.unique:
            self.number = self._get_number_appearing()
        self.ac = self._get_armor_class()
        self.move = self._get_movement()
        self.hd = self._get_hd()
        self.alignment = self._get_alignment()
        self._get_features()
        self.powers = self._get_powers()
        self.immunities = self._get_immunities()
        
    @property
    def description(self):
        desc = []
        if self.colour[0] in ['o', 'u']:
            desc.append('an')
        else:
            desc.append('a')
        desc.append(self.colour)
        desc.append(self.body)
        desc.append('with a %s hide,' % self.hide)
        desc.append('%s eyes,' % self.eyes)
        desc.append('and %s' % self.mouth)
        desc = ' '.join(desc)
        return desc

    def _get_number_appearing(self):
        roll = d(20)
        if roll <= 5:
            return d(2)
        elif roll <= 9:
            return d(3)
        elif roll <= 12:
            return d(4)
        elif roll <= 15:
            return d(6)
        elif roll <= 17:
            return d(8)
        elif roll <= 19:
            return d(10)
        else:
            return xdy(2,6)
            
    def _get_armor_class(self):
        roll = d(20)        
        if roll <= 4:
            return 12
        elif roll <= 8:
            return 13
        elif roll <= 11:
            return 14
        elif roll <= 13:
            return 15
        elif roll <= 15:
            return 16
        elif roll <= 17:
            return 17
        elif roll <= 19:
            return 19
        else:
            return 20
            
    def _get_movement(self):
        """
        Determine type of movement: flying, swimming, etc.
        """
        roll = d(20)
        if roll <= 9:
            move_type = ['land']
        elif roll <= 12:
            move_type = ['land', 'fly']
        elif roll <= 15:
            move_type = ['land', 'swim']
        elif roll <= 17:
            move_type = ['swimming only']
        elif roll <= 19:
            move_type = ['land', 'fly', 'swim']
        else:
            move_type = []
        moves = [(mt, self._get_movement_rate()) for mt in move_type]
        if not moves:
            return "None"
        elif len(moves) == 1 and moves[0][0] == 'land':
            return "%s" % moves[0][1]
        else:
            return " / ".join("%s [%s]" % (d, m) for m, d in moves)
        
    def _get_movement_rate(self):
        """
        Return movement rate in feet.
        """
        roll = d(20)
        if roll == 1:
            return 30
        elif roll <= 3:
            return 60
        elif roll <= 7:
            return 90
        elif roll <= 12:
            return 120
        elif roll <= 15:
            return 150
        elif roll <= 17:
            return 180
        elif roll <= 19:
            return 210
        else:
            return 240
            
    def _get_alignment(self):
        roll = d(8)
        if roll <= 6:
            return 'Chaotic'
        elif roll == 7:
            return 'Neutral [intelligent]'
        else:
            return 'Neutral [unintelligent]'
              
    def _get_features(self):
        self.body = random.choice(Spawn.FORMS)
        roll = d(16)
        if roll >= 15:
            colours = random.sample(Spawn.COLOURS[1:], d(3) + 1)
            colours = ', '.join(colours[:-1]) + ' and ' + colours[-1]
            self.colour = colours
        else:
            self.colour = random.choice(Spawn.COLOURS)
        self.hide = random.choice(Spawn.HIDES)
        self.eyes = d(8) - 1
        if self.eyes == 0:
            self.eyes = 'no'
        elif self.eyes == 7:
            self.eyes = 'multiple/insectile'
        self.mouth = random.choice(Spawn.MOUTHS)
    
    def _get_powers(self):
        roll = d(100)
        if roll <= 84:
            return []
        if roll == 100:
            return random.sample(Spawn.POWERS, 2)
        else:
            return [random.choice(Spawn.POWERS)]
            
    def _get_immunities(self):
        roll = d(20)
        if roll <= 10:
            return []
        elif roll == 20:
            return random.sample(Spawn.IMMUNITIES, 2)
        else:
            return [random.choice(Spawn.IMMUNITIES)]
        
    def _get_hd(self):
        roll = d(20)
        if roll <= 3:
            return 1
        elif roll <= 6:
            return 2
        elif roll <= 9:
            return 3
        elif roll <= 11:
            return 4
        elif roll <= 13:
            return 5
        elif roll <= 15:
            return 6
        elif roll <= 17:
            return 7
        else:
            return roll - 10
    
    FORMS = ['annelidoid', 'plant', 'fungoid', 'batrachian', 'arachnoid', 
            'quadruped', 'octopoid', 'octopoid', 'insectoid', 'crustacean', 
            'amoeboid', 'amoeboid', 'arboreoid', 'avioid', 'icthyoid', 
            'hexapod', 'anthropoid', 'ophidioid', 'ooze/slime', 'ooze/slime']
       
    COLOURS = ['colourless', 'white', 'black', 'blue', 'purple', 'red', 
              'organge', 'yellow', 'green', 'dolm', 'ulfire', 'jale',
              'brown', 'gray']            
    
    HIDES = ['smooth', 'smooth', 'smooth', 'suckered', 'suckered', 'suckered',
             'scaled', 'scaled', 'feathered', 'furred']
    
    MOUTHS = ['no mouth', 'multiple mouths', 'a toothed mouth', 
              'a beaked mouth', 'a suckered mouth', 
              'a circular gaping maw']
              
    POWERS = [
       "Its touch causes paralysis.",
       "The sight of it drives insane.",
       "The sight of it makes opponents flee in fear.",
       "The creature has a breath weapon.",
       "After a successful attack the creature automatically does 1 die damage per round due to blood drain.",
       "Its gaze causes confusion",
       "The creature is extremely cold: 1 die damage per round to all within 20'",
       "The creature poisonous.",
       "Its touch causes sickness (lose 1 Con / day until dead).",
       "Its touch turns anyone to slime.",
       "The creature has 2-9 heads.",
       "The creature surprises on 1-4 on a d6.",
       "The creature shoots spikes (1 die damage).",
       "The creature is extremely hot: 1 die damage per round to all within 20'",
       "The creature is psionic: (1-8 powers, 1-8 times per day)"
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
