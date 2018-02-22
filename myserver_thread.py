# coding=utf-8
import socket
from threading import Thread
import re













class My_server(object):
    def __init__(self):
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.my_socket.bind(('', 20000))

    def run(self):
        self.my_socket.listen(100)
        while True:
            client_socket, addres = self.my_socket.accept()
            print addres
            new_massage = Thread(target=self.my_recv,args=(client_socket,))
            new_massage.start()

    def my_recv(self,new_socket):
        while True:
            massage = new_socket.recv(1024)
            if len(massage) > 0:
                #h = massage.decoding("gb2312")
                print massage
                #re.search("")

                new_socket.send('haha')
            else:

                print("client is closed")
                break
        new_socket.close()

def main():
    p = My_server()
    p.run()


if __name__ == "__main__":
    main()