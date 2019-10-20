import socket               # Import socket module
import os

host = socket.gethostname() # Get local machine name
port = 12364                # Reserve a port for your service.
while True:
    s = socket.socket()         # Create a socket object
    s.connect((host, port))
    print s.recv(2048)
    packet = raw_input("Message");
    s.send(packet)
    s.close()                     # Close the socket when done
    os.system("cls");
