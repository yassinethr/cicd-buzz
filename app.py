import os
from flask import Flask
from buzz.buzzgenerator import BuzzGenerator

app = Flask(__name__)
buzz_generator = BuzzGenerator()


@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += buzz_generator.generate_buzz()
    page += '</h1></body></html>'
    return page


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
