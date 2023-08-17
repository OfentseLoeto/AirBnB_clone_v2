#!/usr/bin/python3
"""
setting up the development environment, which is used for testing
and debugging code before deploying it to production.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', methods=['GET'])
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
