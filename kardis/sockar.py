import socket
import threading

# Sunucu bilgileri (sunucuya bağlanmak için)
HOST = 'localhost'
PORT = 12345

# Sunucudan gelen mesajları alma fonksiyonu
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Sunucudan gelen mesaj: {message}")
        except:
            print("Bağlantı koptu!")
            client_socket.close()
            break

# İstemciyi başlatan fonksiyon
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))  # Sunucuya bağlan

    # Sunucudan gelen mesajları dinle
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    # Kullanıcıdan mesaj al ve sunucuya gönder
    while True:
        message = input("Mesajınızı yazın: ")
        client_socket.send(message.encode('utf-8'))

# İstemciyi başlat
start_client()