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

@app.route("/risk/isclientknown", methods=['GET'])
def getIsClientKnown():
    mac_address = request.args.get('mac', None)
    return jsonify(Controller.isClientKnown(mac_address))
    

@app.route("/risk/isipknown", methods=['GET'])
def getIsIpKnown():
    ip = request.args.get('ip', None)
    return jsonify(Controller.isIpTypeOf(ip,IpType.known))
    


@app.route("/risk/isipinternal", methods=['GET'])
def getIsIpInternal():
    ip = request.args.get('ip', None)
    return jsonify(Controller.isIpTypeOf(ip,IpType.internal))
    


@app.route("/risk/lastsuccessfullogindate", methods=['GET'])
def getLastSuccessfulLoginDate():
    userid = request.args.get('username', None)
    result = Controller.getLastSuccessfulLoginDate(userid)
    if len(result) > 0:
        return jsonify(result[0].split()[0])
    else:
        return 'NA'


@app.route("/risk/LastFailedLoginDate", methods=['GET'])
def getLastFailedLoginDate():
    userid = request.args.get('username', None)
    result = Controller.getLastFailedLoginDate(userid)
    if len(result) > 0:
        return jsonify(result[0].split()[0])
    else:
        return 'NA'


@app.route("/risk/failedlogincountlastweek", methods=['GET'])
def getFailedLoginCountLastWeek():
    return jsonify(len(Controller.getFailedLoginCountLastWeek()))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)