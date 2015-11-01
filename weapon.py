import random
from flask import render_template

from dice import d

class Weapon(object):
    """
    Generate random space alien armaments.
    """
    def __init__(self):
        roll = d(20)
        if 1 <= roll <= 7:
            weapon = 'Pistol'
        elif 8 <= roll <= 13:
            weapon = 'Rifle'
        elif 14 <= roll <= 17:
            weapon = 'Bazooka'
        elif 18 <= roll <= 19:
            weapon = 'Canon'
        else:
            weapon = 'Tank'
            
        self.weapon = weapon
        self.range = Weapon.TYPE[weapon]['range']
        self.damage = Weapon.TYPE[weapon]['damage']
        self.charges = Weapon.TYPE[weapon]['charges']
    
        self.pattern = random.choice(Weapon.PROJECTION_PATTERN)
        
        roll = d(10)
        if 1 <= roll <= 6:
            self.projection_type = random.choice(Weapon.ELECTROMAGNETIC)
        elif 7 <= roll <= 9:
            self.projection_type = random.choice(Weapon.SPECTRAL) + " spectral energy"
        else:
            self.projection_type = None
            self.special = random.choice(Weapon.SPECIAL)
            if '/' in self.special:
                self.special = random.choice(self.special.split('/'))
        
        if self.projection_type == 'Cosmic Radiation':
            self.damage += 2
        elif self.projection_type == 'Gamma Radiation':
            self.damage += 1
        
        self.element = random.choice(Weapon.ELEMENT)

    TYPE = {
        'Pistol': {"range": "300'", "damage": 1, "charges": "d12"},
        'Rifle': {"range": "1000''", "damage": 2, "charges": "d8"},
        'Bazooka': {"range": "3000'", "damage": 4, "charges": "d6"},
        'Canon': {"range": "20 miles'", "damage": 5, "charges": "d4"},
        'Tank': {"range": "10 miles", "damage": 4, "charges": "d4"},
    }

    PROJECTION_PATTERN = [
        "Pulse (3 inch long pulses)",
        "Pulse (3 inch long pulses)",
        "Pulse (3 inch long pulses)",
        "Beam (line shaped)",
        "Beam (line shaped)",
        "Beam (line shaped)",
        "Beam (line shaped)",
        "Ray (cone-shaped)",
        "Ray (cone-shaped)",
        "Emitter (two settings: 180 degrees or 360 degrees)"
    ]
    
    ELECTROMAGNETIC = [
        "Radio Waves",
        "Infrared Radiation",
        "Ultraviolet Radiation",
        "a Laser" ,
        "Microwaves",
        "X-Rays" ,
        "Gamma Radiation",
        "Cosmic Radiation",
    ]
    
    SPECTRAL = [
        "Jale",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Violet",
        "Dolm",
        "Ulfire",
        "White",
    ]
    
    SPECIAL = [
        "fires acid",
        "shoots Dolm Puddings/shoots Dolm Oozes/shoots Jale Slime/shoots Ulfire Jelly",
        "generates Cold energy",
        "is a powerful flame thrower",
        "shoots hardening foam",
        "is an Insanity beam",
        "shoots lightning bolts",
        "is a logic ray",
        "is a paralyzation beam",
        "is a plasma gun",
        "is a polymorph ray",
        "is a shrinking ray",
        "is a sonic ray",
        "is a stun gun",
        "is a teleportation ray",
        "shoots webs",
    ]
    
    ELEMENT = [
        "Hydrogen (double damage to Red Men)",
        "Helium (double damage to Green Men)",
        "Lithium (half damage to Yellow Men)",
        "Beryllium (half damage to Orange Men)",
        "Boron (double damage to Ulfire Men)",
        "Carbon (half damage to Purple Men)",
        "Nitrogen (double damage to Jale Men)",
        "Oxygen (half damage to Blue Men)",
        "Fluorine (half damage to Ulfire Men)",
        "Neon (double damage to Ulfire Men)",
        "Sodium (half damage to Yellow Men)",
        "Magnesium (half damage to Ulfire Men)",
        "Aluminum (double damage to White Men)",
        "Silicon (double damage to Red and Blue Men)",
        "Phosphorus (double damage to Blue and Brown Men)",
        "Sulfur (half damage to White Men)",
        "Chlorine (half damage to Red Men)",
        "Argon (double damage to Blue Men)",
        "Potassium (double damage to Bone Men, half to Orange)",
        "Calcium (double damage to Ulfire Men)",
        "Scandium (double damage to White Men)",
        "Titanium (double damage to Jale and Dolm Men)",
        "Vanadium (double damage to Yellow Men)",
        "Chromium (half damage to Purple Men)",
        "Manganese (half damage to Dolm Men)",
        "Iron (half damage to Brown Men)",
        "Cobalt (double damage to Brown Men)",
        "Nickel (half damage to Ulfire Men)",
        "Copper (half damage to Bone Men)",
        "Zinc (half damage to Red Men)",
        "Gallium (double damage to Orange Men)",
        "Germanium (half damage to Green Men)",
        "Arsenic (half damage to Black Men)",
        "Selenium (double damage to Brown Men)",
        "Bromine (half damage to Brown Men)",
        "Krypton (double damage to Red Men)",
        "Rubidium (double damage to White Men)",
        "Strontium (double damage to Dolm Men)",
        "Yttrium (half damage to Orange Men)",
        "Zirconium (half damage to Blue Men)",
        "Niobium (half damage to Brown Men)",
        "Molybdenum (half damage to Jale Men)",
        "Technetium (double damage to Purple Men)",
        "Ruthenium (half damage to Red Men)",
        "Rhodium (double damage to Yellow Men)",
        "Palladium (double damage to Black Men)",
        "Silver (half damage to Yellow Men)",
        "Cadmium (double damage to Orange Men)",
        "Indium (half damage to Bone Men)",
        "Tin (double damage to Yellow Men, half to Black Men)",
        "Antimony (half damage to Blue Men)",
        "Tellurium (half damage to Dolm Men)",
        "Iodine (double damage to Purple Men)",
        "Xenon (half damage to Purple Men)",
        "Cesium (half damage to Jale Men)",
        "Barium (half damage to White Men)",
        "Lanthanum (half damage to Red Men)",
        "Cerium (double damage to Red Men)",
        "Praseodymium (half damage to Green Men)",
        "Neodymium (half damage to Jale Men, double to Bone Men)",
        "Promethium (half damage to Green Men)",
        "Samarium (half damage to Jale Men)",
        "Europium (double damage to Purple Men)",
        "Gadolinium (half damage to Black Men)",
        "Terbium (half damage to White Men)",
        "Dysprosium (double damage to Dolm Men)",
        "Holmium (half damage to Yellow Men, double to Brown Men)",
        "Erbium (double damage to Ulfire Men)",
        "Thulium (double damage to Green Men, half to Brown Men)",
        "Ytterbium (half damage to Black Men)  ",
        "Lutetium (half damage to White Men)",
        "Hafnium (half damage to Orange Men)",
        "Tantalum (double damage to Bone Men)",
        "Tungsten (double damage to Jale Men)",
        "Rhenium (half damage to Bone Men)",
        "Osmium (double damage to White Men)",
        "Iridium (half damage to Dolm Men)",
        "Platinum (double damage to Orange Men)",
        "Gold (double damage to Purple Men)",
        "Mercury (double damage to Jale Men)",
        "Thallium (half damage to Purple Men)",
        "Lead (double damage to Dolm Men)",
        "Bismuth (half damage to Green Men)",
        "Polonium (double damage to Green Men)",
        "Astatine (double damage to Green Men)",
        "Radon (double damage to Yellow Men)",
        "Francium (double damage to Orange Men)",
        "Radium (double damage to Black Men)",
        "Actinium (double damage to Blue Men)",
        "Thorium (half damage to Blue Men)",
        "Protactinium (half damage to Ulfire Men)",
        "Uranium (double damage to Black Men)",
        "Neptunium (half damage to Dolm Men)",
        "Plutonium (double damage to Black Men)",
    ]