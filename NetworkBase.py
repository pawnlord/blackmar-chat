import socket               # Import socket module

import sys
import os
# import thread module 
from _thread import *
import threading

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name

if len(sys.argv) <= 2:
    port = 12345                # Reserve a port for your service.
else:
    port = sys.argv[2]                # Reserve a port for your service.

s.bind((host, port))        # Bind to the port
host_ip = socket.gethostbyname(socket.gethostname()) 

#get addresses of admins
admins = ""
try:
    ad_file = open("admins.list", "r+")
    admins = ad_file.read()
    if admins == "":
        ad_file.write(host_ip)
        admins = ad_file.read()
    ad_file.close()
except FileNotFoundError:
    ad_file = open(log_name + ".log", "w+")
    ad_file.write(host_ip)
    admins = ad_file.read()
    ad_file.close()


s.listen(5)                 # Now wait for client connection.
removed_channel = ""

def thread(c, addr):
   global s, admins, removed_channel
   # Get log for general channel
   log_str = ""
   log_name = "log#general"
   try:
        log = open(log_name + ".log", "r+")
        log_str = log.read()
        if log_str == "":
            log.write("===Beginning Of Chat History in Channel: " + log_name[4:] + "===\n")
        log.close()
   except FileNotFoundError:
       #create general if not found
       log = open(log_name + ".log", "w+")
       log.write("===Beginning Of Chat History in Channel: " + log_name[4:] + "===\n")
       log_str = log.read()
       log.close()    
   name = addr[0]
   while True:
      # send only the last 2048 of the log in the channel
      if log_name == removed_channel:
         log_name = "log#general"
         log = open(log_name + ".log", "r")
         log_str = log.read()
         log.close()
          
      if len(log_str) > 2048:
         c.send(log_str[len(log_str)-2048:].encode('utf-8'))
      else:
         c.send(log_str.encode('utf-8'))
      #get message         
      msg = c.recv(1024).decode('utf-8')
      print (msg)
      #make sure we can check message
      msg + " "
      #if it is not a command, add it to the log
      if msg[0] != '/':
         log = open(log_name + ".log", "a")
         log.write(name + ": "+ msg + "\n")
         log.close()
         log = open(log_name + ".log", "r")
         log_str = log.read()
         log.close()
      else:
         #if they are an admin, give them special permissions
         if addr[0] in admins:
            if msg[:6] == "/addc-":
                #add channel
                log_name = "log#" + msg[6:]
                log = open(log_name + ".log", "w+")
                log.write("===Beginning Of Chat History in Channel: " + log_name[4:] + "===\n")
                log.close()
                log = open(log_name + ".log", "r")
                log_str = log.read()
                log.close()
            if msg[:8] == "/addadm-":
                #add admin
                ad_file = open("admins.list", "r+")
                ad_file.write(msg[8:])
                admins = ad_file.read()
            if msg[:8] == "/remc" and log_name != "log#general":
                #remove channel
                removed_channel = log_name;
                os.remove(log_name+".log")
                log_name = "log#general"
         #fetch unread messages
         if msg == "/r ":
            pass
         #exit
         elif msg == "/e ":
            log = open(log_name + ".log", "a")
            log.write(name + ": Logged Out\n")
            log.close()
            c.send("LOGGEDOUT");
            break;
         #change name without logging (name non verbose)
         elif msg[:5] == "/nnv-":
            name = msg[5:len(msg)]
         #change channel
         elif msg[:4] == "/cc-":
            log_name = "log#" + msg[4:len(msg)]
            print(log_name)
            try:
                log = open(log_name + ".log", "r+")
                log.close()
            except FileNotFoundError:
                print(name + " Failed to go to channel " + log_name)
                log_name = "log#general"    
            log = open(log_name + ".log", "r")
            log_str = log.read()
            log.close()
         #change name with logging
         elif msg[:3] == "/n-":
            log = open(log_name + ".log", "a")
            log.write(name + ": Changed their name to ")
            name = msg[3:len(msg)]
            log.write(name + "\n")
            log.close()
            log = open(log_name + ".log", "r")
            log_str = log.read()
            log.close()
   c.close()
   # Close the connection

while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   start_new_thread(thread, (c, addr,)) # Spin new thread to have multiple connections
s.close()
