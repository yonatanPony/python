# Client
import socket

#constract the pip with ipv4 and tcp connection. can also leave empty
m_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9090
ip = "10.0.20.49"
#Blook comanned that gets server ip and port
m_c.connect((ip, port))
#sent and recive data
m_c.send("Some info and THIS IS PONY!")
#pacet size. uselly 1024/2048/4096
m_c.recv(4096)

#Importent to close so you cant be followed back0
m_c.close()
