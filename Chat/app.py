from api import api
from flask import Flask, render_template, Response, request, jsonify


app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/")
def main():
    mes = api.getMessages1()

    return render_template("mesages.html", mes=mes)

@app.route("/getmessages")
def getmessages():
    u1 = request.args.get("u1")
    u2 = request.args.get("u2")

    result = api.getMsgU(u1, u2)["messages"]
    result.reverse()
   
    new = ""
    for _ in result:
        new += f'<div class="message-row {_[0]}"><div class="message-content"><img src="static/img/pp.jpg" /><div class="message-text">{_[1]}</div><div class="message-date">16 Mayıs</div></div></div>'

    return new

@app.route("/postMessage")
def postMessageas():
    return "sa"

@app.route("/postMessage", methods=["POST"])
def postMessages():
    message = request.form.get("message")
    fromu = request.form.get("from")
    to = request.form.get("to")
    api.postMessage(fromu, to, message)

    return "True"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)