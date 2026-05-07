import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()
print("Connected:", addr)

filename = client.recv(1024).decode()

file = open("received_" + filename, "wb")

data = client.recv(1024)

while data:
    file.write(data)
    data = client.recv(1024)

file.close()

print("File received successfully")

client.close()
server.close()