from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QMetaObject, Qt
import sys
import random
from datetime import datetime


class Ui_Chatroom(object):
    def __init__(self, tunnel ,app=-1,win=-1,exec=True):

        self.colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Black", "White", "Brown", "Gold", "Silver", "Gray"]
        self.animals = ["Dog", "Cat", "Lion", "Tiger", "Elephant", "Monkey", "Bear", "Falcon", "Hawk", "Chicken", "Cheetah", "GOAT", "Shark"]

        
        self.sendButton = None 
        self.lineEdit = None   
        self.tunnel = tunnel
        
        if app == -1:
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = app
        
        if win == -1:
            self.win = QtWidgets.QWidget()
        else:
            self.win = win

        if exec:
            self.loginUI(self.win)

            self.win.show()
            sys.exit(self.app.exec_())
            
    def loginUI(self, loginWindow):
        self.loginWindow = loginWindow
        self.loginWindow.setObjectName("Form")
        self.loginWindow.resize(573, 99)
        horizontalLayout = QtWidgets.QHBoxLayout(self.loginWindow)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        self.usernameLine = QtWidgets.QLineEdit(self.loginWindow)
        self.usernameLine.setObjectName("lineEdit")
        verticalLayout.addWidget(self.usernameLine)
        
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.loginButton1 = QtWidgets.QPushButton(self.loginWindow)
        self.loginButton1.setObjectName("pushButton_2")
        self.loginButton1.setText("Login")
        self.loginButton1.clicked.connect(lambda: self.openChatUI())

        horizontalLayout_2.addWidget(self.loginButton1)
        
        self.loginButton2 = QtWidgets.QPushButton(self.loginWindow)
        self.loginButton2.setObjectName("pushButton")
        self.loginButton2.setText("Randomize")
        self.loginButton2.clicked.connect(lambda: self.randomizer())
        horizontalLayout_2.addWidget(self.loginButton2)
        verticalLayout.addLayout(horizontalLayout_2)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem1)
        horizontalLayout.addLayout(verticalLayout)

        self.loginWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.loginWindow)
        
    def openChatUI(self): 
        self.username = self.usernameLine.text()
        if len(self.username) < 6:
            self.usernameLine.clear()
            self.usernameLine.setPlaceholderText("Please enter at least 6 characters")
            return

        self.tunnel.startConnect(self.username)
        self.chatWindow = QtWidgets.QWidget()  # Create the chat window
        self.chatUi() 
        self.sendButton.clicked.connect(lambda: self.tunnel.send(self.lineEdit.text()))  # Connect sendButton to send function
        self.chatWindow.show()
        self.loginWindow.hide() 
    
    def randomizer(self):
        random_color = random.choice(self.colors)
        random_animal = random.choice(self.animals)

        random_number = random.randint(0, 999)

        numba = str(random_number).zfill(3)

        # Concatenate the random parts to form the username
        ranus = f"{random_color}{random_animal}{numba}"
        self.usernameLine.setText(ranus)
   
    def chatUi(self):
        self.chatWindow.setObjectName("Chatroom")
        self.chatWindow.resize(908, 473)

        horizontalLayout_4 = QtWidgets.QHBoxLayout(self.chatWindow)
        horizontalLayout_4.setObjectName("horizontalLayout_4")

        gridLayout = QtWidgets.QGridLayout()
        gridLayout.setObjectName("gridLayout")

        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")

        self.disconnectButton = QtWidgets.QPushButton(self.chatWindow)
        self.disconnectButton.setObjectName("pushButton_2")
        self.disconnectButton.setText("Disconnect")
        self.disconnectButton.clicked.connect(lambda: self.disconnect())

        verticalLayout.addWidget(self.disconnectButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        gridLayout.addLayout(verticalLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.chatWindow)
        self.lineEdit.setObjectName("lineEdit")
        
        gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)
        
        self.sendButton = QtWidgets.QPushButton(self.chatWindow)
        self.sendButton.setToolTip("")
        self.sendButton.setToolTipDuration(-1)
        self.sendButton.setObjectName("pushButton")
        self.sendButton.setText("Send")

        
        self.lineEdit.returnPressed.connect(lambda: self.sendButton.click())
        # self.sendButton.clicked.connect(lambda: self.send(self.lineEdit.text()))
        
        gridLayout.addWidget(self.sendButton, 2, 1, 1, 1)


        self.textBrowser = QtWidgets.QTextBrowser(self.chatWindow)
        self.textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        horizontalLayout_4.addLayout(gridLayout)


        self.chatWindow.show()
        QtCore.QMetaObject.connectSlotsByName(self.chatWindow)

    def disconnect(self):
        self.chatWindow.close()
        self.loginWindow.show()
        self.tunnel.on_disconnect(self.tunnel)
        
    def receive(self, data):
        # c = datetime.now()
        # current_time = c.strftime('%H:%M:%S')
        stamp = f"{data[3]}:{data[0]}:"
        self.textBrowser.append(f"<p style='color:{data[2]}'>{stamp} <span class:'text' style='color:black'> {data[1]} </span> </p>")
        # self.textBrowser.moveCursor(QtGui.QTextCursor.End)
        # print(self.textBrowser.setHtml)
        
    def chat_receive(self,data) -> None:
        # self.textBrowser.clear()
        # self.textBrowser.setHtml(data)
        QMetaObject.invokeMethod(self.textBrowser, "setHtml", Qt.QueuedConnection, QtCore.Q_ARG(str, data))
        
    def getHtml(self) -> str:
        return self.textBrowser.toHtml()

       
# app = QtWidgets.QApplication(sys.argv)
# win = QtWidgets.QWidget()

# ui = Ui_Chatroom()
# # ui.chatUi(win)
# ui.loginUI(win)

# win.show()
# sys.exit(app.exec_())



