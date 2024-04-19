from PyQt5 import QtCore, QtWidgets 
import socketio
from client_ui import Ui_Chatroom


class Tunnel:
    global sio
    sio = socketio.Client()     
    
    def __init__(self):
        try:
            sio.connect('http://127.0.0.1:8000/ ')
        except:
            print("Connection Error")
                           
    @sio.event
    def connect():
        print('Connected to the server!')

    @sio.event
    def disconnect():
        print('Disconnected from the server.')

    @sio.event
    def chat_message(data):
        print('Message received from server:', data)
        
    def send(self, message):
        sio.emit('chat_message', message)


if __name__ == "__main__": 
    tunel = Tunnel()
    ui = Ui_Chatroom()
    ui.sendButton.clicked.connect(lambda: tunel.send(ui.lineEdit.text()))
    
    
    
    
# # Keep the client running (optional)
# # sio.wait() 
