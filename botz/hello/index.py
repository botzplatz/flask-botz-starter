from flask import Flask

app = Flask(__name__)


def say_hello():
    return "Hello World"


class BotzApp:
    def __init__(self, app):
        self.app = app

    def init_routes(self):
        @self.app.route("/", methods=["POST"])
        def root():
            return say_hello()
