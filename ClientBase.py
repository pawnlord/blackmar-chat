import socket               # Import socket module
import os
import sys
import _thread
import threading
import time
import msvcrt

def timed_raw_input(prompt, timeout=5.0):
    print(prompt)
    finishat = time.time() + timeout
    result = []
    while True:
        if msvcrt.kbhit():
            result.append(msvcrt.getche())
            if result[-1] == '\r':   
                return ''.join(result)
        else:
            if time.time() > finishat and result == []:
                return ""
host = socket.gethostname() # Get local machine name
has_port = False
name = "GUEST"
port = 0
channel = ""
has_channel = False
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
    elif sys.argv[i] == "-ch":
        i+=1
        channel = sys.argv[i]
        has_channel = True;
if not has_port:
    port = 12356

s = socket.socket()         # Create a socket object
s.connect((host, port))
print(s.recv(2048))
s.send(bytes("/nnv-" + name, 'utf-8'))
if has_channel:
    print(s.recv(2048).decode('utf-8'))
    s.send(("/cc-"+channel).encode('utf-8'))
os.system("cls");
while True:
    print(s.recv(2048).decode('utf-8'))
    packet = input("Message: ");
    if packet == "":
        s.send("/r".encode('utf-8'))
        pass
    s.send(packet.encode('utf-8'))
    os.system("cls");
    if packet == "/e":
        s.recv(2048)
        s.close()                     # Close the socket when done
        break;

