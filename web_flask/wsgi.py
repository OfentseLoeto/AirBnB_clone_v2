#!/usrbin/python3
"""
Setting up production application server with Gunicorn on web-01, port 5000
"""

from 0-hello_route import app

if __name__ == '__main__':
    app.run()
