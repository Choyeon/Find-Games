import socket
import threading
from tkinter import *

class Server(threading.Thread):
    num = 0
    def __init__(self,ns):
        super().__init__()
        self.ns = ns

    def run(self):
        name = self.ns.recv(9)
        game_name = self.ns.recv(4399)
        name = name.decode("utf-8")
        game_name = game_name.decode("utf-8")
        game_name = eval(game_name)
        print(name)
        with open(str(name),"a+") as f:
            for temp in game_name:
                f.write(str(temp)+"\n")
                print(temp)

        Server.num += 1
        print(Server.num,"/",72)


def main():
    # 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    s.bind(("", 4399))
    # 设置为监听套接字
    s.listen(8)
    while True:
        ns, dest_ip = s.accept()
        Server(ns).start()
        print("目前已经记录的人数: ",Server.num)

if __name__ == '__main__':
    main()