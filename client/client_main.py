from PyQt5 import QtCore, QtWidgets 
import socketio
from client_ui import Ui_Chatroom
import sys


class Tunnel:
    global sio
    sio = socketio.Client()  
    def __init__(self):
        self.isconnected = False
    
    def startConnect(self):
        try:
            sio.connect('http://127.0.0.1:8000/ ')
        except:
            print("Connection Error")
        self.isconnected = True
                           
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
    tunnel = Tunnel()
    ui = Ui_Chatroom(tunnel)
    
   
   
   
# # Keep the client running (optional)
# # sio.wait() 
