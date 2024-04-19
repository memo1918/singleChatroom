from PyQt5 import QtCore, QtGui, QtWidgets 
import sys

class Ui_Chatroom(object):
    def loginUI(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 99)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
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

        self.pushButton_2 = QtWidgets.QPushButton(Chatroom)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Disconnect")
        self.pushButton_2.clicked.connect(self.disconnect)

        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(Chatroom)
        self.pushButton.setToolTip("")
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Send")
        self.pushButton.clicked.connect(self.send)
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

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



