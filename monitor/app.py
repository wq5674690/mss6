#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psutil
import datetime
import socket

#-------------------------------------------------------------------
# socket客户端
sk = socket.socket()
sk.connect(("192.168.8.110", 8888))  # 主动初始化与服务器端的连接
while True:
    send_data = input("输入发送内容:")
    sk.sendall(bytes(send_data, encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(("接收内容：", accept_data)))
sk.close()
