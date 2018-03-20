from flask import Flask
from DegreeOfSeperation import findSep
app = Flask(__name__)

@app.route("/brickHack4/<string:name>")
def initialize(name):
    deg = findSep()
    return deg.findID(name)

if __name__ == '__main__':
    app.run()
