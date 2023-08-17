#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', methods=['GET'])
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
