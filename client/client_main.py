from PyQt5 import QtCore, QtWidgets 
import socketio
from client_ui import Ui_Chatroom
import sys
from profanityfilter import ProfanityFilter

sio = socketio.Client()  

class Tunnel:
    global sio
    def __init__(self):
        self.isconnected = False
        self.ui=None
        self.profanityfilter = ProfanityFilter()
    
    def startConnect(self,username):
        if self.isconnected:
            return
            
        try:
            sio.connect('http://127.0.0.1:8000/',{"username":username})
        except:
            print("Connection Error")
            return
        self.isconnected = True
        
    def send(self,message):
        if message.strip():
            blurred_message = self.profanityfilter.censor(message)
            self.ui.lineEdit.clear()
            sio.emit('chat_message', blurred_message)
    
    def sendUi(self,message):
        self.send(message)
        
    def disconnect(self):
        sio.disconnect()
 
    @staticmethod
    def on_connect(instance):
        print('Connected to the server!')

    @staticmethod
    def on_disconnect(instance):
        instance.isconnected = False
        print('Disconnected from the server.')

    @staticmethod
    def on_chat_message(instance,data):
        instance.ui.receive(data)
        
    @staticmethod
    def on_getChat_history(instance):
        data = instance.ui.textBrowser.toHtml()
        # print(data)
        sio.emit('chat_history',data)

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    
    tunnel = Tunnel()
    ui = Ui_Chatroom(tunnel,app,win,exec=False)
    tunnel.ui = ui
    
    sio.on('connect', lambda: Tunnel.on_connect(tunnel))
    sio.on('disconnect', lambda: Tunnel.on_disconnect(tunnel))
    sio.on('chat_message', lambda data: Tunnel.on_chat_message(tunnel,data))
    sio.on('getChat_history', lambda: Tunnel.on_getChat_history(tunnel))

    ui.loginUI(win)
    win.show()
    sys.exit(app.exec_())
    
   
   
   
# # Keep the client running (optional)
# # sio.wait() 
