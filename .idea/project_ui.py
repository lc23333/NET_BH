from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from PyQt5.QtWidgets import *
# from PyQt5 import QtGui, QtCore
import login
import my_operate
import login_ui
import chat_ui

class project_ui():
    def __init__(self):

        self.login_ui=login_ui.login_ui()
        self.login_ui.login_signal.connect(self.turn_to_chat)

    def turn_to_chat(self,id):
        self.chat_ui=chat_ui.chat_ui(id)
if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    my_project_ui=project_ui()
    # my_login_ui=login_ui()
    # my_login_ui = TNWLogin()
    # my_login_ui.show()
    sys.exit(app.exec())