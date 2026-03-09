from flask import Flask
from routes.route import *

app = Flask(__name__)
from routes.route import *



if __name__ == "__main__":
    app.run(debug = True)
    