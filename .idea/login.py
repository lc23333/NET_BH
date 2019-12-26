# -*- coding: UTF-8 -*-
from socket import *
import re

def login(id,pwd='net2019'):
    s=socket(AF_INET,SOCK_STREAM)
    s.connect(('166.111.140.57',8000))
    login_msg=id+'_'+pwd
    s.sendall(login_msg.encode('utf-8'))
    login_back=s.recv(1024).decode('utf-8')
    s.close()
    return login_back=='lol'#判断是否登陆成功

def online(id):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('166.111.140.57', 8000))
    id_msg='q'+id
    s.sendall(id_msg.encode('utf-8'))
    online_back=s.recv(1024).decode('utf-8')
    s.close()
    return online_back#!='n'#判断好友是否在线

def logout(id):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('166.111.140.57', 8000))
    logout_msg='logout'+id
    s.sendall(logout_msg.encode('utf-8'))
    logout_msg=s.recv(1024).decode('utf-8')
    s.close()
    return logout_msg=='loo'#判断是否登出成功

if __name__=='__main__':
    print(login('2017011566'))
    # id_list = ['2017011566']
    # id_list.append(('3017011566'))
    print(online('2017011566'))
    # print(logout('2017011566'))