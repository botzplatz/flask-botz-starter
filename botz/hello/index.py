from os import getenv
from dotenv import load_dotenv
from botzapp import BotzApp

load_dotenv()

name = "Hello World"
PORT = getenv("PORT", 5001)


def say_hello():
    return name


start = BotzApp.gen_botz_app(port=PORT, name=name, gen_success_response=say_hello)
