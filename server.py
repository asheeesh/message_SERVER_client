import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

name = socket.gethostname()
port = 4444
sock.bind((name,port))




    
while True:
    sock.listen(1)
    sc , addr = sock.accept()
    print("this client is connected")
    while True:

        chat = input("enter the data:")
        data = chat.encode('UTF-8')
        sc.send(data)
 #   sc.close()