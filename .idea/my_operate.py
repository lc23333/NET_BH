# -*- coding: UTF-8 -*-

'''
在这一部分定义各类操作，例如发送文字、发送文件等，同时在这一部分也管理好进程
'''

from socket import *
import threading
import time
import login
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
import os
import json

def send_msg_thread(data,ip,port):#这个函数是发送msg的线程，每发送一条消息开一个新的线程
    data=json.dumps(data)

    client=socket(AF_INET,SOCK_STREAM)
    print(ip,port)
    client.connect((ip,port))
    client.sendall(data.encode('utf-8'))

    client.close()

def send_msg(src_id,des_ids,msg,port):
    data={}
    data['type']='msg'#数据类型、发送者id、接受者ids、消息内容、当前时间
    data['src_id']=src_id
    data['des_ids']=des_ids
    data['msg']=msg
    data['time']=int(round(time.time() * 1000))


    send_num=0
    for id in des_ids:
        ip=login.online(id)
        print('ip is '+ip)
        if ip is 'n':
            print('the user is not online')
        else:
            t=threading.Thread(target=send_msg_thread,args=(data,ip,port))
            t.start()
            send_num+=1
    return [data,send_num]#返回数据全部内容以及发送成功的数目

def send_file_thread(data,ip,port):
    data=json.loads(data)
    file_name=data['file_name']#首先获取完整的路径名
    data['file_name']=os.path.basename(file_name)#获取文件名用于显示
    data=json.dumps(data)

    try:
        client=socket(AF_INET,SOCK_STREAM)#建立tcp连接
        client.connect((ip,port))
        client.send(data.encode('utf-8'))
        back_msg=client.recv(3)
        if back_msg==b'ACK':#若接收到了ack返回信号则发送文件
            print('have receved a ACK')
            with open(file_name,'rb') as send_file:#读取本地文件
                while True:
                    part_file=send_file.read(1024)#将本地文件都读取到part_file中去
                    if not part_file:
                        break;
                    client.sendall(part_file)
                print('have sent'+' '+file_name)
        else:
            print('no ack back')
    except error as e:
        print("error collecting:"+format(e))
    finally:
        client.close()

def send_file(src_id,des_ids,file_name,port):
    data = {}
    data['type'] = 'file'  # 数据类型、发送者id、接受者ids、文件完整路径、当前时间
    data['src_id'] = src_id
    data['des_ids'] = des_ids
    data['file_name'] = file_name
    data['time'] = int(round(time.time() * 1000))
    data=json.dumps(data)

    send_num=0
    for id in des_ids:
        online_msg=login.online(id)
        print(online_msg)
        if online_msg is 'n':
            print(id+' is not online')
        else:
            t=threading.Thread(target=send_file_thread,args=(data,online_msg,port))
            t.start()
            send_num+=1
            print('has reached the send_file_thread')
    return [data,send_num]

def deal_msg_thread(server_sock,msg_recv_signal):#另开一个处理消息的进程
    buff=1024
    msg=b''
    while True:#将所有的data内容都读取
        msg_part=server_sock.recv(buff)
        msg+=msg_part
        if len(msg_part)<buff:
            break
    msg=json.loads(msg.decode('utf-8'))#将接收到的data转化为字典格式
    print('has received a msg')
    print(msg)
    # print(msg['type']=='file')
    if msg['type'] == 'file':
        print('start receive a file')
        file_name=msg['file_name']
        server_sock.sendall(b'ACK')
        print('has sent a ACK')
        with open('data/recv/'+file_name,'wb') as recv_file:
            part_file=server_sock.recv(1024)
            while part_file:
                recv_file.write(part_file)
                part_file=server_sock.recv(1024)
            print('has received a file')

    msg_recv_signal.emit(msg)#发射信号，用以进行在ui中的操作，当接收到一条信息的时候需要进行一系列操作

def accept_msg_thread(server):
    while True:#这是一个循环进程，一旦接收到一个连接请求再进入处理信息的进程
        client_sock,_=server.accept()
        t=threading.Thread(target=deal_msg_thread,args=(client_sock,1))
        t.start()
        print('start a receiving proceed')

class server_thread(QThread):
    msg_recv_signal=pyqtSignal(object)#定义一个信号，一旦接收到消息发送信号
    def __init__(self,port,parent=None):
        super().__init__(parent)
        self.stop_event=threading.Event()
        self.port=port
    def run(self):
        self.server=socket(AF_INET,SOCK_STREAM)
        self.server.bind(('0.0.0.0',self.port))
        self.server.listen(10)
        while not self.stop_event.is_set():
            try:
                self.server.settimeout(0.1)
                client_sock,_=self.server.accept()
            except timeout:
                pass
            except:
                raise
            else:
                t=threading.Thread(target=deal_msg_thread,args=(client_sock,self.msg_recv_signal))
                t.start()
    def Stop_event(self):
        self.stop_event.set()



if __name__=='__main__':
    id_list=['2017011566']
    # id_list.append(('3017011566'))
    # s=socket(AF_INET,SOCK_STREAM)
    # s.bind(('0.0.0.0',6666))
    # s.listen(5)
    # print('waiting for connecting')
    # t=threading.Thread(target=accept_msg_thread,args=(s,))
    # t.start()

    text=''
    while text!='q':
        text=input('sending a message:')
        send_msg('3017011566',id_list,text,6666)
        # send_msg('2017011566', id_list, text, 6666)
    # file_path='D:\THU大学学习\大三上\计算机网络及其应用-贾庆山\课件\lecture01.pptx'
    # print(os.path.isfile(file_path))
    # if os.path.isfile(file_path):
    #     print('comin')
    #     send_file('2017011566',id_list,file_path,6666)

