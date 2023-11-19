from socket import *
from threading import *

clients = []
names = []

def clientThread(client):
    bayrak = True
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if bayrak:
                names.append(message)
                print(message, 'bağlandı')
                bayrak = False
            for c in clients:
                if c != client:
                    index = clients.index(client)
                    name = names[index]
                    c.send((name + ':' + message).encode('utf8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            name = names[index]
            names.remove(name)
            print(name+ 'çıktı')
            break
        

server = socket(AF_INET, SOCK_STREAM)

ip = "SENINIPV4 ADRESİN"
port = 6666
server.bind((ip, port))
server.listen()
print('Server Dinlemede')


while True:
    client, adress = server.accept()
    clients.append(client)
    print('Bağlantı Yapıldı', adress[0] + ':' + str(adress[1]))
    thread = Thread(target = clientThread, args=(client,))
    thread.start()            
