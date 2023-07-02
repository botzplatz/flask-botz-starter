from os import getenv
from dotenv import load_dotenv
from botzapp import gen_botz_app

load_dotenv()

name = "Hello World"
PORT = getenv("PORT", 5001)


def call():
    def say_hello():
        return name

    start = gen_botz_app(name=name, gen_success_response=say_hello)
    start(PORT)
