# client
import socket

port = 1
ip = input("Enter ip to scan: \n")
while port < 10000:
    try:
        s = socket.socket()
        s.settimeout(0.00015)
        s.connect((ip, port))
        print("The port " + str(port) + " is open")
        # To search an SSH port
        bunner = s.recv(2048)
        if bunner.lower().find("ssh") != -1:
            print("SSH is in: " + str(port))
            print(bunner)

    except:
        pass
    finally:
        port += 1
        s.close()
