from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return "SocketIO Server Running"

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('response', {'message': 'Connected to Flask-SocketIO!'})

@socketio.on('mensaje')
def handle_message(data):
    print(f"Message received: {data}")
    emit('response', {'message': f"Message '{data}' received!"})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)