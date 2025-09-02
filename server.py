import threading
import socket

ip = '127.0.0.1'
port = 8728

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
namamu = []
clients = []
server.listen()

def broadcast(pesan):
    for client in clients:
        client.send(pesan)

# Menerima Koneksi Client
def receive():
    while True:
        print('Server sedang berjalan...')
        client, address = server.accept()
        print(f'Koneksi tersambung dengan alamat {str(address)}')
        client.send('nama?'.encode())
        nama = client.recv(1024)
        namamu.append(nama)
        clients.append(client)
        print(f'Client bernama {nama} telah tersambung'.encode())
        broadcast(f'>> Server : Selamat Datang {nama} '.encode())
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Koneksi Client
def handle_client(client):
    while True:
        try:
            pesan = client.recv(1024)
            broadcast(pesan)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nama = namamu[index]
            broadcast(f'{nama} telah keluar dari chat!'.encode())
            namamu.remove(nama)
            break

if __name__ == "__main__":
    receive()
