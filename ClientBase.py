import socket               # Import socket module
import os
import sys
host = socket.gethostname() # Get local machine name
if len(sys.argv) <= 2:
    port = 12365                # Reserve a port for your service.
else:
    port = sys.argv[2]                # Reserve a port for your service.

s = socket.socket()         # Create a socket object
s.connect((host, port))
while True:
    print s.recv(2048)
    packet = raw_input("Message: ");
    s.send(packet)
    if packet == "/e":
        s.close()                     # Close the socket when done
        break;
    os.system("cls");

