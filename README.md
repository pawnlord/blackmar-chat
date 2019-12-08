# Blackmar  
A simple server that can make a chat room  
  
## Using the client  
to use the blackmar client, there are very few arguements:  
- -p: the port you want to use  
- -n: the name you want to use on the client  
- -a: the adress of the server  
when chatting, you can use a few commands  
to use a command, you put a slash infront of the command name  
a list of commands:  
- r: get the current conversation  
- e: loggout  
- n-: change name  
- nnv-: change name without it being saved in the conversation  
## Using the server  
to set up blackmar, you have to make an empty log file (named log.log) that will be used as your chat history, and put in text saying something like "===Beginning of Chat History===" with a newline to make it work properly  
to use the blackmar server after setting up the log all you have to do is run NetworkBase.py with python2, with the first arguement after python2 being an open port you plan on using for your server that the client wil put into the -p arguement.