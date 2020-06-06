#######################################################
# 
# RecieveConnections.py
# Python implementation of the Class RecieveConnections
# Generated by Enterprise Architect
# Created on:      19-May-2020 6:21:05 PM
# Original author: Natha Paquette
# 
#######################################################
import socket
class RecieveConnections:
    def __init__(self):  
        pass
    def listen(self, sock, pipe):
        #listen for client connections
        sock.listen(1000)
        while True:
            try:
                #establish the socket variables
                client, address = sock.accept()
                #wait to receive client
                data = client.recv(1024)
                print('client connected')
                #establish the socket array containing important information about the client
                socket = [client, address, data.decode('utf-8')]
                self.retrieveNecessaryInformation(socket, pipe)
                
            except Exception as e:
                print('error')
                print(e)

    def retrieveNecessaryInformation(self, rawConnectionInformation, pipe):
        print('datapassed through pipe') 
        #this adds the important client data to the data pipe allowing it to be recieved by the orchestrator
        pipe.send(rawConnectionInformation)