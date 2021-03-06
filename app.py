from flask import Flask, request, make_response, redirect, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecret"
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def mesaj_al(mesaj):
    if mesaj == "User has connected":
        send(request.remote_addr+"+ bagli")

    else:
            
        print("Mesaj:", mesaj)
        send(request.remote_addr+": "+mesaj.replace("<", "&lt;"), broadcast=True)


@app.route("/")
def ana():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0")
