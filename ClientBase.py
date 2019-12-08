import socket               # Import socket module
import os
import sys
host = socket.gethostname() # Get local machine name
has_port = False
name = "GUEST"
port = 0
for i in range(len(sys.argv)):
    if sys.argv[i] == "-p":
        i+=1
        port = int(sys.argv[i])# Reserve a port for your service.
        has_port = True
    elif sys.argv[i] == "-n":
        i+=1
        name = sys.argv[i]
    elif sys.argv[i] == "-a":
        i+=1
        host = sys.argv[i]
if not has_port:
    port = 12365

s = socket.socket()         # Create a socket object
s.connect((host, port))
print s.recv(2048)
s.send("/nnv-" + name)
os.system("cls");

while True:
    print s.recv(2048)
    packet = raw_input("Message: ");
    if packet == "":
        s.send(" ")
        pass
    s.send(packet)
    os.system("cls");
    if packet == "/e":
        s.close()                     # Close the socket when done
        break;

