#coding utf-8

import socket 

import threading

class GestionDesUtilisateurs(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn=conn
        
    def run(self):
        data = self.conn.recv(2048)    
        data = data.decode("utf8")
        print (data)
        
#__#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_


host, port = ('',5566) #5566 correspond au port à ecouter a modifier en fonction du port ouvert pour le service

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print ("le seveur es démarré   !!!   ")

while True : 
    socket.listen()     # nombre d 'ehec de connexion admissible  
    conn , address = socket.accept()
    print ("un client vient de se connecter .....")
    
    my_thread = GestionDesUtilisateurs (conn)
    my_thread.start()
conn.close()
socket.close()
