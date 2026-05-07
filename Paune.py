import socket

client = socket.socket()
client.connect(("localhost", 5000))

filename = "prayas.txt"

client.send(filename.encode())

file = open(filename, "rb")

data = file.read(1024)

while data:
    client.send(data)
    data = file.read(1024)

file.close()

client.close()