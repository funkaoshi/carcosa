
from flask import render_template, Flask

import colour
import dice
import dinosaur
import monster
import settlement
import spawn
import weapon
import weird


app = Flask(__name__)
app.config.from_prefixed_env()


def random_hex():
    return "%02d%02d" % (dice.d(40), dice.d(40))


@app.route("/")
def index():
    return render_template(
        "index.html",
        hex_a=random_hex(),
        hex_b=random_hex(),
        hex_c=random_hex(),
        hex_d=random_hex(),
        hex_e=random_hex(),
        hex_f=random_hex(),
        spawn=spawn.Spawn(),
        settlement=settlement.Settlement(),
        dinosaur=dinosaur.Dinosaur(),
        monster=monster.Monster(),
        title=settlement.Leader.get_name(colour.colour()),
        weird=weird.WierdGenerator().weird(),
    )


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/roll/")
def roll():
    return render_template("roll.html", dcarcosa=dice.carcosa())


@app.route("/settlement/")
def make_settlement():
    return render_template(
        "settlement.html", hex=random_hex(), settlement=settlement.Settlement()
    )


@app.route("/title/")
def make_title():
    return render_template(
        "title.html",
        hex=random_hex(),
        title=settlement.Leader.get_name(colour.colour()),
    )


@app.route("/spawn/")
def make_spawn():
    return render_template("spawn.html", hex=random_hex(), spawn=spawn.Spawn())


@app.route("/monster/")
def make_monster():
    return render_template("monster.html", hex=random_hex(), monster=monster.Monster())


@app.route("/dinosaur/")
def make_dinosaur():
    return render_template(
        "dinosaur.html", hex=random_hex(), dinosaur=dinosaur.Dinosaur()
    )


@app.route("/weird/")
def make_weird():
    return render_template(
        "weird.html", hex=random_hex(), weird=weird.WierdGenerator().weird()
    )


@app.route("/weapon/")
def make_weapon():
    return render_template("weapon.html", hex=random_hex(), weapon=weapon.Weapon())


@app.route("/random/", defaults={"count": 32})
@app.route("/random/<int:count>/")
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
        elif roll <= 88:
            random_hexes.append(dinosaur.Dinosaur())
        else:
            random_hexes.append(monster.Monster())
    return render_template(
        "random.html", hexes=random_hexes, count=int(len(random_hexes) / 2)
    )


if __name__ == "__main__":
    app.run("0.0.0.0")
