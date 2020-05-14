import sys
import socket

client = socket.socket()
host = 'localhost'
port = 8889

# Connecting
client.connect((host,port))
#print ('Connected to ...')

message = 'How much gold do you have?'
while True:
    client.send(message.encode('ascii'))

    data = client.recv(1024)
    print('Recibido:', str(data.decode('ascii')))

    ans = input('')
