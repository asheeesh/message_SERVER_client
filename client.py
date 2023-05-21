from pickle import TRUE
import socket
from uu import decode
name = socket.gethostname()
port =4444
try:
    sock =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("sucessfully created the socket")
except:
    print("socket is not created")
try:
    sock.connect((name,port))
    print("sucessfully connected")
except:
    print("not connected")    
while True:
    
    
    data = sock.recv(1024).decode('UTF-8')         
    print(data)