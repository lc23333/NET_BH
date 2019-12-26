from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from PyQt5.QtWidgets import *
# from PyQt5 import QtGui, QtCore
import login
import my_operate


class login_ui(QWidget):
    login_signal=pyqtSignal(str)#定义一个signal传递的是id信息
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(400,300)
        self.verticalLayout = QVBoxLayout()

        self.lineEdit_id=QLineEdit('',self)
        # self.lineEdit_id.setFixedSize(300,20)
        self.lineEdit_id.setPlaceholderText("please enter the id")
        self.verticalLayout.addWidget(self.lineEdit_id)

        # self.lineEdit_pwd = QLineEdit('')
        # self.lineEdit_pwd.setPlaceholderText("please enter the password")
        # self.verticalLayout.addWidget(self.lineEdit_pwd)

        self.pushButton_enter=QPushButton('',self)
        self.pushButton_enter.setText("enter")
        self.verticalLayout.addWidget(self.pushButton_enter)

        self.setLayout(self.verticalLayout)
        self.pushButton_enter.clicked.connect(self.pushButton_enter_clicked)

        self.show()
    def pushButton_enter_clicked(self):
        id=self.lineEdit_id.text()
        if login.login(id):
            self.login_signal.emit(str(id))
        else:
            QMessageBox.about(self,'Error','Please enter the right id or password')

# class TNWLogin(QWidget):
#     get_id_signal = QtCore.pyqtSignal(str)
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         label = QLabel('Enter ID to login.', self)
#         label.setFixedSize(400, 100)
#         label.move(0, 40)
#         label.setAlignment(QtCore.Qt.AlignCenter)
#         label.setStyleSheet('font-size:18pt;')
#
#         self.idTextLine = QLineEdit('', self)
#         self.idTextLine.setFixedSize(200, 40)
#         self.idTextLine.move(100, 150)
#         self.idTextLine.setAlignment(QtCore.Qt.AlignCenter)
#         self.idTextLine.setFocus(True)
#         self.idTextLine.setText('')
#         self.idTextLine.setStyleSheet('font-size:18pt;')
#         regexp = QtCore.QRegExp('^\d{1,10}$')
#         validator = QtGui.QRegExpValidator(regexp)
#         self.idTextLine.setValidator(validator)
#         self.idTextLine.returnPressed.connect(self.login)
#
#         self.setFixedSize(400, 250)
#         self.center()
#         self.setWindowTitle('Login TNW')
#         self.show()
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#     def login(self):
#         Id = self.idTextLine.text()
#         if len(Id) == 10 and login.login(Id):
#             self.get_id_signal.emit(str(Id))
#             self.close()
#         else:
#             QMessageBox.about(self, 'Error', 'Please enter a right ID.')

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    my_login_ui=login_ui()
    # my_login_ui = TNWLogin()
    # my_login_ui.show()
    sys.exit(app.exec())
