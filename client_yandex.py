import socket
import threading
from time import sleep

yandex_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("87.250.250.242", 443)
yandex_sock.connect(address)

data_send = b"GET / HTTP/1.1\r\nHost:ya.ru\r\n\r\n"
yandex_sock.send(data_send)

data_receiv = b""

def receiving():
    global data_receiv
    while True:
        data_piece = yandex_sock.recv(1024)
        data_receiv += data_piece
        
stream = threading.Thread(target=receiving)
stream.start()

sleep(4)
print(data_receiv)
yandex_sock.close()