## -*- coding: utf-8 -*-

from PyQt5.QtGui import *

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
friend_list=['3017011566']
# # QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))
#
#
# # class user_group_ui(QTabWidget):
# #     def __init__(self, parent=None):
# #         super(user_group_ui, self).__init__(parent)
# #
# #         toolButton1 = QToolButton()
# #         toolButton1.setText(self.tr("颜楠"))
# #         toolButton1.setIcon(QIcon("data/pic/qq_head.png"))
# #         toolButton1.setIconSize(QSize(60, 60))
# #         toolButton1.setAutoRaise(True)
# #         toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
# #
# #         toolButton2 = QToolButton()
# #         toolButton2.setText(self.tr("夏天"))
# #         toolButton2.setIcon(QIcon("data/pic/qq_head.png"))
# #         toolButton2.setIconSize(QSize(60, 60))
# #         toolButton2.setAutoRaise(True)
# #         toolButton2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
# #
# #         toolButton3 = QToolButton()
# #         toolButton3.setText(self.tr("迪迪"))
# #         toolButton3.setIcon(QIcon("data/pic/qq_head.png"))
# #         toolButton3.setIconSize(QSize(60, 60))
# #         toolButton3.setAutoRaise(True)
# #         toolButton3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
# #
# #         groupbox1 = QGroupBox()
# #         vlayout1 = QVBoxLayout(groupbox1)
# #         # vlayout1.setMargin(10)
# #         vlayout1.setAlignment(Qt.AlignCenter)
# #         vlayout1.addWidget(toolButton1)
# #         vlayout1.addWidget(toolButton2)
# #         vlayout1.addStretch()
# #
# #         groupbox2 = QGroupBox()
# #         vlayout2 = QVBoxLayout(groupbox2)
# #         # vlayout2.setMargin(10)
# #         vlayout2.setAlignment(Qt.AlignCenter)
# #         vlayout2.addWidget(toolButton3)
# #         vlayout2.addStretch()
# #
# #         groupbox3 = QGroupBox()
# #
# #         toolbox1 = QToolBox()
# #         toolbox1.addItem(groupbox1, self.tr("我的好友"))
# #         toolbox1.addItem(groupbox2, self.tr("lover"))
# #         toolbox1.addItem(groupbox3, self.tr("黑名单"))
# #
# #         toolbox2 = QToolBox()
# #
# #         self.addTab(toolbox1, "联系人")
# #         self.addTab(toolbox2, "群/讨论组")
#
#
#
# class user_group_ui(QTabWidget):
#     def __init__(self, parent=None):
#         super(user_group_ui, self).__init__(parent)
#         self.init_ui()
#     def init_ui(self):
#         # self.toolButton1 = QToolButton(self)
#         # self.toolButton1.clicked.connect(self.show_chat)
#         # self.toolButton1.setText(self.tr("颜楠"))
#         # self.toolButton1.setIcon(QIcon("data/pic/qq_head.png"))
#         # self.toolButton1.setIconSize(QSize(60, 60))
#         # self.toolButton1.setAutoRaise(True)
#         # self.toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#         #
#         # self.toolButton2 = QToolButton(self)
#         # self.toolButton2.setText(self.tr("夏天"))
#         # self.toolButton2.setIcon(QIcon("data/pic/qq_head.png"))
#         # self.toolButton2.setIconSize(QSize(60, 60))
#         # self.toolButton2.setAutoRaise(True)
#         # self.toolButton2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#         #
#         # # self.toolButton3 = QToolButton()
#         # # self.toolButton3.setText(self.tr("迪迪"))
#         # # self.toolButton3.setIcon(QIcon("data/pic/qq_head.png"))
#         # # self.toolButton3.setIconSize(QSize(60, 60))
#         # # self.toolButton3.setAutoRaise(True)
#         # # self.toolButton3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#         #
#         # self.groupbox1 = QGroupBox(self)
#         # self.vlayout1 = QVBoxLayout(self.groupbox1)
#         # # vlayout1.setMargin(10)
#         # self.vlayout1.setAlignment(Qt.AlignCenter)
#         # self.vlayout1.addWidget(self.toolButton1)
#         # self.vlayout1.addWidget(self.toolButton2)
#         # self.vlayout1.addStretch()
#         #
#         # # self.groupbox2 = QGroupBox(self)
#         # # vlayout2 = QVBoxLayout(self.groupbox2)
#         # # # vlayout2.setMargin(10)
#         # # vlayout2.setAlignment(Qt.AlignCenter)
#         # # vlayout2.addWidget(self.toolButton3)
#         # # vlayout2.addStretch()
#         #
#         # # self.groupbox3 = QGroupBox(self)
#         #
#         # self.toolbox1 = QToolBox(self)
#         # self.toolbox1.addItem(self.groupbox1, self.tr("我的好友"))
#         # # self.toolbox1.addItem(self.groupbox2, self.tr("lover"))
#         # # self.toolbox1.addItem(self.groupbox3, self.tr("黑名单"))
#         #
#         # self.toolbox2 = QToolBox(self)
#         #
#         # self.addTab(self.toolbox1, "联系人")
#         # self.addTab(self.toolbox2, "群/讨论组")
#         pass
#
#     def add_friend(self,ids):
#         # toolButton1 = QToolButton()
#         # toolButton1.setText(self.tr(id))
#         # toolButton1.setIcon(QIcon("data/pic/qq_head.png"))
#         # toolButton1.setIconSize(QSize(60, 60))
#         # toolButton1.setAutoRaise(True)
#         # toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#         # self.vlayout1.addWidget(self.toolButton1)
#         # self.toolbox1.addItem(self.groupbox1, self.tr("我的好友"))
#
#         for id in ids:
#             print(id)
#             self.toolButton1 = QToolButton(self)
#             self.toolButton1.clicked.connect(self.show_chat)
#             self.toolButton1.setText(self.tr(id))
#             self.toolButton1.setIcon(QIcon("data/pic/qq_head.png"))
#             self.toolButton1.setIconSize(QSize(60, 60))
#             self.toolButton1.setAutoRaise(True)
#             self.toolButton1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#
#             self.groupbox1 = QGroupBox(self)
#             self.vlayout1 = QVBoxLayout(self.groupbox1)
#             # vlayout1.setMargin(10)
#             self.vlayout1.setAlignment(Qt.AlignCenter)
#             self.vlayout1.addWidget(self.toolButton1)
#             # self.vlayout1.addWidget(self.toolButton2)
#             self.vlayout1.addStretch()
#             self.toolbox1 = QToolBox(self)
#             self.toolbox1.addItem(self.groupbox1, self.tr("我的好友"))
#             # self.toolbox1.addItem(self.groupbox2, self.tr("lover"))
#             # self.toolbox1.addItem(self.groupbox3, self.tr("黑名单"))
#
#         self.toolbox2 = QToolBox(self)
#
#         self.addTab(self.toolbox1, "联系人")
#         self.addTab(self.toolbox2, "群/讨论组")
#     def show_chat(self):
#         QMessageBox.about(self, 'show', 'This is your chat window')
class friend_group_ui(QScrollArea):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWidgetResizable(True)
        self.area_vbox=QVBoxLayout()
        self.area_vbox.addStretch()
        self.area_widget=QWidget()
        self.area_widget.setLayout(self.area_vbox)

        self.setWidget(self.area_widget)

        self.show()

class friend_button(QPushButton):
    def __init__(self, friend):
        super().__init__()
        self.friend=friend
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(120, 50)
        if len(self.friend) > 1:
            self.setText('Group: \n' + self.friend[0] + ' ...')
        else:
            self.setText(self.friend[0])





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myqq = friend_group_ui()
    # myqq.setWindowTitle("chat_2019")
    # myqq.show()
    # # myqq.add_friend('2017011566')
    # friend='2017011566'
    # friend_list.append(friend)
    # myqq.add_friend(friend_list)
    app.exec_()

