import socket, threading

chat_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chat_server.bind(('127.0.0.1', 55555))
chat_server.listen()

clients_connections = []
nicknames = []

def send_to_all(message):
    for connection in clients_connections:
        connection.send(message)
        
def handler_clients_messages(connection):
    while True:
        try:
            message = connection.recv(1024)
            send_to_all(message)
        except:
            temp_index = clients_connections.index(connection)
            clients_connections.remove(connection)
            connection.close()
            send_to_all('{} left chat!'.format(nicknames[temp_index]).encode('ascii'))
            nicknames.remove(nicknames[temp_index])
            break 

def main_server_stream():
    while True:
        connection, address = chat_server.accept()
        print('Connect with {}'.format(str(address)))
    
        connection.send('NICK'.encode('ascii'))
        nickname = connection.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients_connections.append(connection)
    
        print('Nickname is {}'.format(nickname))
        send_to_all('{} is joined to chat!'.format(nickname).encode('ascii'))
        connection.send('Connection to chat server created!'.encode('ascii'))
    
        main_server_stream = threading.Thread(target=handler_clients_messages, args = (connection,))
        main_server_stream.start()
    
print('listening...')
main_server_stream()