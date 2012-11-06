import random

from flask import render_template, Flask

import dice
import settlement
import spawn
import monster
import weird

# configuration
SECRET_KEY = 'Y\xf6\xf2j\xc9\xc5\xbc\xde{\xae\x9a\xc8\x8dZ0\x9e\x14\xb6\x90\xd7\x02\x03\xf0\x1a'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def random_hex():
    return "%02d%02d" % (dice.d(40), dice.d(40))

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html",
            hex_a=random_hex(), hex_b=random_hex(),
            hex_c=random_hex(), hex_d=random_hex(),
            spawn=spawn.Spawn(), settlement=settlement.Settlement(),
            monster=monster.Monster(), weird=weird.WierdGenerator().weird())

@app.route('/settlement/', methods=['GET'])
def make_settlement():
   return render_template("settlement.html",
           hex=random_hex(), settlement=settlement.Settlement())

@app.route('/spawn/', methods=['GET'])
def make_spawn():
   return render_template("spawn.html",
           hex=random_hex(), spawn=spawn.Spawn())

@app.route('/monster/', methods=['GET'])
def make_monster():
   return render_template("monster.html",
           hex=random_hex(), monster=monster.Monster())

@app.route('/weird/', methods=['GET'])
def make_weird():
   return render_template("weird.html",
           hex=random_hex(), weird=weird.WierdGenerator().weird())

@app.route('/random/', defaults={'count': 32})
@app.route('/random/<int:count>/', methods=['GET'])
def make_random(count):
    weird_gen = weird.WierdGenerator()
    random_hexes = []
    for i in range(count):
        roll = dice.d(100)
        if roll <= 40:
            random_hexes.append(weird_gen.weird())
        elif roll <= 70:
            random_hexes.append(settlement.Settlement())
        elif roll <= 83:
            random_hexes.append(spawn.Spawn())
        else:
            random_hexes.append(monster.Monster())
    return render_template("random.html", hexes=random_hexes,
                           count=int(len(random_hexes)/2))


if __name__ == '__main__':
    app.run("0.0.0.0")
