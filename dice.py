import sys
import random

def d(die):
    return random.randint(1, die)

def xdy(x,y):
    return sum(d(y) for i in range(x))

def xdcarcosa(x):
    twenty = d(20)
    if 1 <= twenty <= 4:
        rolled = 4
    elif 5 <= twenty <= 8:
        rolled = 6
    elif 9 <= twenty <= 12:
        rolled = 8
    elif 13 <= twenty <= 16:
        rolled = 10
    elif 16 <= twenty <= 20:
        rolled = 12
    print({'result': xdy(x, rolled), 'dice': rolled})

def carcosa(n=1):
    rolls = dict((x, d(x)) for x in [4, 6, 8, 10, 12, 20])
    twenty = rolls[20]
    if 1 <= twenty <= 4:
        rolled = 4
    elif 5 <= twenty <= 8:
        rolled = 6
    elif 9 <= twenty <= 12:
        rolled = 8
    elif 13 <= twenty <= 16:
        rolled = 10
    elif 16 <= twenty <= 20:
        rolled = 12
    return {'rolls': rolls, 'rolled': rolled, 'result': rolls[rolled]}


if __name__ == '__main__':
    print(xdcarcosa(int(sys.argv[1])))
