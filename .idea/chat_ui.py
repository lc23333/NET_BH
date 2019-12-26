import time
import json
import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import login
import my_operate
#
# class project_ui(QMainWindow):
#     def __init__(self):
#         self.login_widget=
class chat_ui(QMainWindow):
    def __init__(self,id):
        super().__init__()
        self.id=id
        self.now_friends=[]
        self.init_ui()
        # self.read_now_friend_file()

        self.listen_msg(6666)#用来监听接收到的消息
        self.port=6666
    def init_ui(self):
        # self.setFixedSize(600,500)
        # self.verticalLayout=QVBoxLayout()
        #
        # self.plain_text_edit=QPlainTextEdit('',self)
        # self.plain_text_edit.setFixedSize(200,300)
        # self.verticalLayout.addWidget(self.plain_text_edit)
        #
        # self.setLayout(self.verticalLayout)
        #定义按钮并定义槽函数===================================================================
        self.send_msg_btn=QPushButton('发送消息')
        self.send_msg_btn.setFixedSize(120,30)
        self.send_msg_btn.clicked.connect(self.send_msg_btn_clicked)

        self.send_file_btn=QPushButton('发送文件')
        self.send_file_btn.setFixedSize(120,30)
        self.send_file_btn.clicked.connect(self.send_file_btn_clicked)

        self.add_friend_btn=QPushButton('添加好友')
        self.add_friend_btn.setFixedSize(120,30)
        self.add_friend_btn.clicked.connect(self.add_friend_btn_clicked)

        self.add_group_btn=QPushButton('添加群组')
        self.add_group_btn.setFixedSize(120,30)
        self.add_group_btn.clicked.connect(self.add_group_btn_clicked)

        self.check_friend_btn=QPushButton('查看好友状态')
        self.check_friend_btn.setFixedSize(120,30)
        self.check_friend_btn.clicked.connect(self.check_friend_btn_clicked)

        #定义聊天框与发送框==================================================================
        self.msg_area=QScrollArea()#这一部分定义来聊天框
        self.msg_area.setWidgetResizable(True)
        self.msg_area_vbox=QVBoxLayout()
        self.msg_area_vbox.addStretch()
        self.msg_area_widget=QWidget()
        self.msg_area_widget.setLayout(self.msg_area_vbox)
        self.msg_area.setWidget(self.msg_area_widget)

        self.text_edit=QTextEdit()#这一部分定义发送框
        # self.setFixedSize(100,100)
        self.text_edit.setFixedHeight(100)

        self.conv_label=QLabel()#定义聊天框的框头
        self.conv_label.setText(self.id)
        self.conv_label.setWordWrap(True)

        #定义联系人与群组区域====================================================================
        self.friend_area=QScrollArea()#这是联系人与群组区域
        self.friend_area.setWidgetResizable(True)
        self.friend_area_vbox=QVBoxLayout()
        self.friend_area_vbox.addStretch()
        self.friend_area_widget=QWidget()
        self.friend_area_widget.setLayout(self.friend_area_vbox)
        self.friend_area.setWidget(self.friend_area_widget)

        #定义布局区域将上述部件布局================================================================
        self.vbox_r1=QHBoxLayout()
        self.vbox_r1.addWidget(self.send_msg_btn)
        self.vbox_r1.addWidget(self.send_file_btn)
        self.vbox_r1.addWidget(self.check_friend_btn)

        self.vbox_r=QVBoxLayout()
        self.vbox_r.addWidget(self.conv_label)
        self.vbox_r.addWidget(self.msg_area)
        self.vbox_r.addLayout(self.vbox_r1)
        self.vbox_r.addWidget(self.text_edit)

        self.vbox_l1=QVBoxLayout()
        self.vbox_l1.addWidget(self.add_friend_btn)
        self.vbox_l1.addWidget(self.add_group_btn)

        self.vbox_l=QHBoxLayout()
        self.vbox_l.addWidget(self.friend_area)
        self.vbox_l.addLayout(self.vbox_l1)


        self.hbox=QHBoxLayout()
        self.hbox.addLayout(self.vbox_l,0)
        self.hbox.addLayout(self.vbox_r,1)
        self.project_widget=QWidget()
        self.project_widget.setLayout(self.hbox)
        self.setCentralWidget(self.project_widget)
        self.resize(1000,600)
        self.setMinimumSize(600,400)
        self.setWindowTitle('chat')
        self.show()

        #定义按钮事件
    def send_msg_btn_clicked(self):
        print('发送消息')
        pass
    def send_file_btn_clicked(self):
        print('发送文件')
        pass
    def check_friend_btn_clicked(self):
        print('查看好友信息')
        pass
    def add_friend_btn_clicked(self):
        print('添加好友')
        pass
    def add_group_btn_clicked(self):
        print('添加群组')
        pass
    def friend_btn_clicked(self):
        print('打开聊天界面')
        self.now_friends=self.sender().now_friends

        self.read_msg()#todo:read_msg


    def listen_msg(self,port):
        self.server=my_operate.server_thread(port,self)
        self.server.msg_recv_signal.connect(self.deal_msg)
        self.server.start()
        print('start receving massage')
    def deal_msg(self,data):
        friends=sorted(set([data['src_id']]+data['des_ids']))

        # self.write_msg()
        if friends==sorted(set(self.now_friends+[self.id])):
            print('展示消息')
            self.show_msg(data)
        else:
            print('尚未添加发送消息的好友，直接添加')
            friend_btn=self.add_friend(sorted(set(friends)-set([self.id])),True)
            #添加好友按钮，这一步的作用是如果对于群组没有建立的话，由建立人发一条消息直接建立
    def show_msg(self,data):
        time_msg=time.localtime(data['time']/1000)
        head_msg=data['src_id']+' '+time.strftime("%Y-%m-%d %H:%M:%S",time_msg)
        if data['type']=='msg':
            msg_widget=QWidget()
            msg_hbox=QHBoxLayout()
            msg_vbox=QVBoxLayout()
            msg_widget.setLayout(msg_hbox)

            label_head=QLabel()
            label_head.setText(head_msg)
            label_head.setWordWrap(True)
            msg_vbox.addWidget(label_head)

            label_content=QLabel()
            label_content.setText(data['msg'])
            label_content.setWordWrap(True)
            msg_vbox.addWidget(label_content)

            content_widget=QWidget()
            content_widget.setLayout(msg_vbox)

            if data['src_ip']==self.id:
                msg_hbox.addStretch()
                msg_hbox.addWidget(content_widget,5)
                label_head.setAlignment(Qt.AlignRight)
                label_content.setAlignment(Qt.AlignRight)
            else:
                msg_hbox.addStretch()
                msg_hbox.addWidget(content_widget, 5)
                label_head.setAlignment(Qt.AlignLeft)
                label_content.setAlignment(Qt.AlignLeft)
        elif data['type']=='file':
            msg_widget = QWidget()
            msg_hbox = QHBoxLayout()
            msg_vbox = QVBoxLayout()
            msg_widget.setLayout(msg_hbox)

            label_head = QLabel()
            label_head.setText(head_msg)
            label_head.setWordWrap(True)
            msg_vbox.addWidget(label_head)

            file_btn=QPushButton()
            file_btn.setText(data['file_name'])
            # file_btn.clicked.connect(self.open_file())
            if data['src_id']==self.id:
                file_btn.setEnabled(False)
            msg_vbox.addWidget(file_btn)

            content_widget = QWidget()
            content_widget.setLayout(msg_vbox)

            if data['src_ip'] == self.id:
                msg_hbox.addStretch()
                msg_hbox.addWidget(content_widget, 5)
                label_head.setAlignment(Qt.AlignRight)
                label_content.setAlignment(Qt.AlignRight)
            else:
                msg_hbox.addStretch()
                msg_hbox.addWidget(content_widget, 5)
                label_head.setAlignment(Qt.AlignLeft)
                label_content.setAlignment(Qt.AlignLeft)

    def add_friend(self,friend,judge=True):
        flag=-1
        for i in range(self.friend_area_vbox.count()-1):
            if self.friend_area_vbox.itemAt(i).widget().now_friend==friend:
                flag=i
        if flag==-1:
            my_friend_btn=friend_btn(friend)
            my_friend_btn.clicked.connect(self.friend_btn_clicked)
            count_num=self.friend_area_vbox.count()
            self.friend_area_vbox.insertWidget(count_num-1,my_friend_btn)

            if judge:
                my_friend_btn.clicked.emit()
            return my_friend_btn
        else:
            if judge:
                self.friend_area_vbox.itemAt(flag).widget().clicked.emit()
        return self.friend_area_vbox.itemAt(flag).widget()

#定义一个friend按钮 用来加好友=====================================================================
class friend_btn(QPushButton):
    def __init__(self,now_friend):
        super().__init__()
        self.now_friend=now_friend
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(120,30)
        length=len(self.now_friend)
        if length==1:
            self.setText(self.now_friend[0])
        else:
            self.setText('群组：\n'+self.now_friend[0]+'...')

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    my_chat_ui=chat_ui('2017011566')
    # btn=friend_btn('123')
    # btn.show()
    # my_login_ui = TNWLogin()
    # my_login_ui.show()
    sys.exit(app.exec())