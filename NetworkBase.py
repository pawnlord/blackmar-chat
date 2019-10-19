import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12364               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
log = open("log.log", "r")
log_str = log.read()
log.close()
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send(log_str)
   msg = c.recv(1024)
   print msg
   log = open("log.log", "a")
   log.write(str(addr) + ": "+ msg + "\n")
   log.close()
   log = open("log.log", "r")
   log_str = log.read()
   log.close()
   c.close()                # Close the connection
