import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to the server!')

@sio.event
def disconnect():
    print('Disconnected from the server.')

@sio.event
def chat_message(data):
    print('Message received from server:', data)

# Replace with your server's address and port
sio.connect('http://127.0.0.1:8000/ ')

while True:
    message = input("Enter your message: ")
    sio.emit('chat_message', message) 


# Keep the client running (optional)
# sio.wait() 
