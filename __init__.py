from flask import Flask, jsonify
from localController import MyMethods

Controller = MyMethods()
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return jsonify("hello, world")

@app.route("/hello")
def hello():
    return jsonify(Controller.hellowWorld())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)