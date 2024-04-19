from PyQt5 import QtCore, QtGui, QtWidgets 
import sys

class Ui_Chatroom(object):
    def loginUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 99)
        horizontalLayout = QtWidgets.QHBoxLayout(Form)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout = QtWidgets.QVBoxLayout()
        verticalLayout.setObjectName("verticalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        lineEdit = QtWidgets.QLineEdit(Form)
        lineEdit.setObjectName("lineEdit")
        verticalLayout.addWidget(self.lineEdit)
        
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.loginButton1 = QtWidgets.QPushButton(Form)
        self.loginButton1.setObjectName("pushButton_2")
        horizontalLayout_2.addWidget(self.loginButton1)
        
        self.loginButton2 = QtWidgets.QPushButton(Form)
        self.loginButton2.setObjectName("pushButton")
        horizontalLayout_2.addWidget(self.loginButton2)
        verticalLayout.addLayout(self.horizontalLayout_2)
        
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem1)
        horizontalLayout.addLayout(self.verticalLayout)

        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def chatUi(self, Chatroom):
        Chatroom.setObjectName("Chatroom")
        Chatroom.resize(908, 473)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Chatroom)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.loginButton1 = QtWidgets.QPushButton(Chatroom)
        self.loginButton1.setObjectName("pushButton_2")
        self.loginButton1.setText("Disconnect")
        self.loginButton1.clicked.connect(self.disconnect)

        self.verticalLayout.addWidget(self.loginButton1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.loginButton2 = QtWidgets.QPushButton(Chatroom)
        self.loginButton2.setToolTip("")
        self.loginButton2.setToolTipDuration(-1)
        self.loginButton2.setObjectName("pushButton")
        self.loginButton2.setText("Send")
        self.loginButton2.clicked.connect(self.send)
        self.gridLayout.addWidget(self.loginButton2, 2, 1, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(Chatroom)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.textBrowser = QtWidgets.QTextBrowser(Chatroom)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)


        Chatroom.show()
        QtCore.QMetaObject.connectSlotsByName(Chatroom)

    def disconnect(self):
        print("Disconnected!")
        
    def send(self):
        print("Message sent!")
        
       
       
       
app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QWidget()

ui = Ui_Chatroom()
ui.chatUi(win)
win.show()
sys.exit(app.exec_())



