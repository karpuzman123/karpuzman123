import socket
import threading

# Sunucu bilgileri
HOST = 'localhost'  # Yerel makine üzerinde çalışacak
PORT = 12345        # Port numarası

# Bağlı istemciler için liste
clients = []

# Mesajları diğer istemcilere iletme
def broadcast(message, current_client):
    for client in clients:
        if client != current_client:  # Gönderen istemci hariç diğerlerine ilet
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# İstemcilerden gelen mesajları işleyen fonksiyon
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                print(f"Mesaj alındı: {message.decode('utf-8')}")
                broadcast(message, client)  # Mesajı diğer istemcilere gönder
        except:
            clients.remove(client)
            client.close()
            break

# Sunucuyu başlatan fonksiyon
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Sunucu {HOST}:{PORT} adresinde çalışıyor...")

    while True:
        client, address = server.accept()  # Yeni istemci bağlantısını kabul et
        print(f"{address} bağlandı.")
        clients.append(client)  # İstemciyi listeye ekle
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Sunucuyu başlat
start_server()
