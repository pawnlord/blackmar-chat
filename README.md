# Blackmar  
A simple server that can make a chat room  
  
## Using the client  
to use the blackmar client, there are very few arguements:  
- -p: the port you want to use (automatically 12345)  
- -n: the name you want to use on the client (automatically Guest)  
- -a: the adress of the server (automatically host address)  
  
when chatting, you can use a few commands  
to use a command, you put a / infront of the command name  
  
a list of commands:  
- r: get the current conversation  
- e: loggout  
- n-: change name. arg: new name  
- nnv-: change name without it being saved in the conversation. arg: new name  
- cc-: Change channel. arg: channel name
  
There are also admin commands:  
- addadm-: give someone admin privileges. arg: address of new admin  
- addc-: add channel. arg: channel Name  
- remc-: remove channel. everyone on that channel is booted to general. arg: channel to remove  
  
## Using the server  
To use the blackmar server all you have to do is run NetworkBase.py with python 3, with the first arguement after python being an open port you plan on using for your server that the client will put into the -p arguement (automatically 12345).  