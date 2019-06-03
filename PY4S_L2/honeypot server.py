# Server
import socket

s = socket.socket()
# Basic preferenc for server
port = 6565
s.bind(("0.0.0.0", port))
s.listen(1)
c, addr = s.accept()

# code
print (addr)
command = input("Shell > ")
while command != "exit":
    c.send(command.encode())
    print (c.recv(65535).decode())
    command = input("Shell > ")

c.send("exit".encode())
c.close()
s.close()
