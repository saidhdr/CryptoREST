from flask import Flask, jsonify, request, render_template, Markup, json
from localController import MyMethods, LogFileStructMapper, IpType

Controller = MyMethods()
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    #return jsonify("hello, world")
    return render_template("index.html", title="hello, world", value = "Hej there")


@app.route("/risk")
@app.route("/risk/")
def risk():
    tags = Markup("<b>API List (risk):</b><br />isuserknown?username=userid<br />isclientknown?mac=macaddress<br />isipknown?ip=ipaddress<br />isipinternal?ip=ipaddress<br />lastsuccessfullogindate?username=userid<br />lastfailedlogindate?username=userid<br />failedlogincountlastweek <br />")
    return render_template("index.html", title="hello, world", value = tags)


@app.route("/hello")
def hello():
    return jsonify(Controller.hellowWorld())


@app.route("/getalllog")
def getAllLog():
    return jsonify(Controller.getLatestLog())


@app.route("/risk/isuserknown", methods=['GET'])
def getIsUserKnown():
    userid = request.args.get('username', None)
    #return jsonify(Controller.isUserKnown(userid))
    return render_template("index.html", title="hello, world", value = Controller.isUserKnown(userid))
@app.route("/risk/isclientknown", methods=['GET'])
def getIsClientKnown():
    mac_address = request.args.get('mac', None)
    #return jsonify(Controller.isClientKnown(mac_address))
    return render_template("index.html", title="hello, world", value = Controller.isClientKnown(mac_address))

@app.route("/risk/isipknown", methods=['GET'])
def getIsIpKnown():
    ip = request.args.get('ip', None)
    #return jsonify(Controller.isIpTypeOf(ip,IpType.known))
    return render_template("index.html", title="hello, world", value = Controller.isIpTypeOf(ip,IpType.known))


@app.route("/risk/isipinternal", methods=['GET'])
def getIsIpInternal():
    ip = request.args.get('ip', None)
    #return jsonify(Controller.isIpTypeOf(ip,IpType.internal))
    return render_template("index.html", title="hello, world", value = Controller.isIpTypeOf(ip,IpType.internal))


@app.route("/risk/lastsuccessfullogindate", methods=['GET'])
def getLastSuccessfulLoginDate():
    userid = request.args.get('username', None)
    result = Controller.getLastSuccessfulLoginDate(userid)
    if len(result) > 0:
        #return jsonify(result[0].split()[0])
        return render_template("index.html", title="hello, world", value = result[0].split()[0])
    else:
        #return 'NA'
        return render_template("index.html", title="hello, world", value = 'NA')


@app.route("/risk/lastfailedlogindate", methods=['GET'])
def getLastFailedLoginDate():
    userid = request.args.get('username', None)
    result = Controller.getLastFailedLoginDate(userid)
    if len(result) > 0:
        #return jsonify(result[0].split()[0])
        return render_template("index.html", title="hello, world", value = result[0].split()[0])
    else:
        #return 'NA'
        return render_template("index.html", title="hello, world", value = 'NA')


@app.route("/risk/failedlogincountlastweek", methods=['GET'])
def getFailedLoginCountLastWeek():
    #return jsonify(len(Controller.getFailedLoginCountLastWeek()))
    return render_template("index.html", title="hello, world", value = len(Controller.getFailedLoginCountLastWeek()))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, threaded=True, debug=True)