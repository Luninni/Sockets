import socket
import sys
import threading

# Message Buffer size
MSG_BUFFER = 1024

# Obtaining the arguments using command line
try:
    HOST = sys.argv[1]
except:
    HOST = 'localhost'
try:
    PORT = int(sys.argv[2])
except:
    PORT = 8889    
# Creating the client socket. AF_INET IP Family (v4)
# and STREAM SOCKET Type.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#crea sochet
server.bind((HOST, PORT))
server.listen(6) # numero de clientes que acepta

#Lista de clientes
Identif = []
NameClient = []

while True:
    
    #print ('Client connected to ...')
    client, addr = server.accept()  # Acepting client
    print ('[SERVER] Client' + str(client.getpeername()) + 'connected!')
    msg = client.recv(MSG_BUFFER)
    client.send('Bienvenido','prueba')
    client.close()
    #print('<'+str(sclient.getpeername())+'>: '+ str(msg))
