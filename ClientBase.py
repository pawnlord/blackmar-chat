import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12364                # Reserve a port for your service.
s.connect((host, port))
print s.recv(2048)
packet = raw_input("Message");
s.send(packet)
s.close()                     # Close the socket when done
