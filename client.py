#coding utf-8
import socket

host, port = ('127.0.0.1', 5566)   #'127.0.0.1' = local host pour toutes eles machine, 5566) 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.connect((host,port))
    print ("client connecté") #partie a modifier en fonc de l uti
    
    data = "Bonjour je suis le client " # A passer en input indiquer le nom de l'uti :
    data = data.encode("utf8")
    socket.sendall(data)
    
except ConnectionRefusedError :
    print ("Connextion serveur echouee")
finally:
    socket.close()
