import socket
import threading

nickname = input ("Wath's your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive_messasge_from_server():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write_client_message():
    while True:
        message = '{}: {}'.format(nickname, input('>> '))
        client.send(message.encode('ascii'))
        
receive_messasge_from_server_stream = threading.Thread(target=receive_messasge_from_server)
receive_messasge_from_server_stream.start()

write_client_message_stream = threading.Thread(target=write_client_message)
write_client_message_stream.start()