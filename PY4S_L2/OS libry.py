import os
import sys

'''
#Python Shell
command = raw_input("command: \n")
while command != "exit":
    os.system(command)
    command = raw_input("command: \n")
'''

'''
#The use of sys.argv is to get command from the user
#The [] info is where the argoment will go01
os.system(sys.argv[1])
#what platform are you in
print (sys.platform)
#To do a search in the system
path =  "c:\\"
file = raw_input("Enter File name")
for path,listdir,listfile in os.walk(path):
    if file in listfile:
        print path+"\\"+file
        break
'''

'''
#How to look for files with key word
path = "c:\\"
look = "pass"
for path, listdir, listfile in os.walk(path):
    for filename in  listfile:
        if look.find(look) != -1:
            location = path+"\\"+filename
            openfile= open(location,"r")
            print openfile.read()
            openfile.close()
'''



