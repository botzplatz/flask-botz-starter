from flask import Flask
from botz.hello.index import BotzApp

app = Flask(__name__)
server = BotzApp(app)
server.init_routes()

if __name__ == "__main__":
    app.run(debug=True)  # runs in port 5000 by default
