from flask import Flask


# only accept keyword arguments
def gen_botz_app(*, name: str, port: int, gen_success_response: callable):
    app = Flask(__name__)

    @app.route("/", methods=["POST"])
    def index():
        return gen_success_response()

    def start():
        print(f"Starting {name} on port {port}")
        app.run(debug=True, port=port)

    return start
