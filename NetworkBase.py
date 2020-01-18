import socket               # Import socket module

import sys
# import thread module 
from _thread import *
import threading

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name

if len(sys.argv) <= 2:
    port = 12365                # Reserve a port for your service.
else:
    port = sys.argv[2]                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port

try:
    log = open("log.log", "r+")
    log_str = log.read()
    if log_str == "":
        log.write("===Beginning Of Chat History===")
    log.close()
except FileNotFoundError:
    log = open("log.log", "w+")
    log.write("===Beginning Of Chat History===")
    log_str = log.read()
    log.close()

s.listen(5)                 # Now wait for client connection.

            
def thread(c, addr):
   global log_str, s
   name = addr[0]
   while True:
      if len(log_str) > 2048:
         c.send(log_str[len(log_str)-2048:].encode('utf-8'))
      else:
         c.send(log_str.encode('utf-8'))
         
      msg = c.recv(1024).decode('utf-8')
      print (msg)
      msg + " "
      if msg[0] != '/':
         log = open("log.log", "a")
         log.write(name + ": "+ msg + "\n")
         log.close()
         log = open("log.log", "r")
         log_str = log.read()
         log.close()
      else:
         if msg == "/r ":
            pass
         elif msg == "/e ":
            log = open("log.log", "a")
            log.write(name + ": Logged Out\n")
            log.close()
            log = open("log.log", "r")
            log_str = log.read()
            log.close()
            break;
         elif msg[:5] == "/nnv-":
            name = msg[5:len(msg)]
            
         elif msg[:3] == "/n-":
            log = open("log.log", "a")
            log.write(name + ": Changed their name to ")
            name = msg[3:len(msg)]
            log.write(name + "\n")
            log.close()
            log = open("log.log", "r")
            log_str = log.read()
            log.close()
   c.close()
   # Close the connection

while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   start_new_thread(thread, (c, addr,)) # Spin new thread to have multiple connections
s.close()
