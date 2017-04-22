# Script to receive image data from the Pi

import socket
import R2Protocol

TCP_PORT = 5005
BUFFER_SIZE= 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#TCP_IP = s.getfqdn()
#TCP_IP = '127.0.0.1'
TCP_IP = ''

s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
encoded_data = b''
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: 
		break
	encoded_data = encoded_data + data

decoded_data = R2Protocol.decode(encoded_data)

with open("image.jpeg", "wb") as f:
	f.write(decoded_data["data"])

conn.close()
