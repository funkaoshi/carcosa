import random

COLOURS = [
    "Black", "Blue", "Bone", "Brown", "Dolm", "Green", "Jale",
    "Orange", "Purple", "Red", "Ulfire", "White", "Yellow"
]
def colour():
    return random.choice(COLOURS)

if __name__ == "__main__":
    import sys
    for _ in range(int(sys.argv[1])):
        print colour()
