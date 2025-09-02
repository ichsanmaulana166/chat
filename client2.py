import threading
import socket

nama = input('Masukkan Nama : ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8728))

def client_receive():
    while True:
        try:
            pesan = client.recv(1024).decode()
            if pesan == "nama?":
                client.send(nama.encode())
            else:
                print(pesan)
        except:
            print('Terputus dengan server!')
            client.close()
            break

def client_send():
    while True:
        pesan = f'{nama}: {input("")}'
        client.send(pesan.encode())

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()
send_thread = threading.Thread(target=client_send)
send_thread.start()
