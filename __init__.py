from flask import Flask, jsonify, request
from localController import MyMethods, LogFileStructMapper, IpType

Controller = MyMethods()
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return jsonify("hello, world")


@app.route("/hello")
def hello():
    return jsonify(Controller.hellowWorld())


@app.route("/getalllog")
def getAllLog():
    return jsonify(Controller.getLatestLog())


@app.route("/risk/isuserknown", methods=['GET'])
def getIsUserKnown():
    userid = request.args.get('username', None)
    return jsonify(Controller.isUserKnown(userid))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)