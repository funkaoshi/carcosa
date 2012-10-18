from flask import render_template, Flask

import dice
import settlement
import spawn

# configuration
SECRET_KEY = 'Y\xf6\xf2j\xc9\xc5\xbc\xde{\xae\x9a\xc8\x8dZ0\x9e\x14\xb6\x90\xd7\x02\x03\xf0\x1a'
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

def random_hex():
    return "%2d%02d" % (dice.d(40), dice.d(40))

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", 
            hex_a=random_hex(), spawn=spawn.Spawn(),
            hex_b=random_hex(), settlement=settlement.Settlement())
        
@app.route('/settlement/', methods=['GET'])
def make_settlement():
   return render_template("settlement.html", 
           hex=random_hex(), settlement=settlement.Settlement())
           
@app.route('/spawn/', methods=['GET'])
def make_spawn():
   return render_template("spawn.html", 
           hex=random_hex(), spawn=spawn.Spawn())
           
if __name__ == '__main__':
    app.run("0.0.0.0")
