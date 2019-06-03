#Server
import socket


s = socket.socket()
#Basic preferenc for server
port = 6565
s.bind(("0.0.0.0", port))
s.listen(1)

#Makeing a privet tunnel
client, addr =s.accept()

client.send("Hi, my name is PONY.")
data = client.recv(20484)

client.close()
s.close()