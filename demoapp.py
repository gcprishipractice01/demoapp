from flask import Flask
import socket
demoapp = Flask(__name__)

@demoapp.route('/')
def hostname():
    return socket.gethostname()

if __name__ == '__main__':
    demoapp.run()
