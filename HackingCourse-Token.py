#! python3
#!/usr/bin/python3
'''
This is a token request which I use for requesting a course link.
'''

import socket
import random

wordlist = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']
text = []
ip = '104.248.39.146'
port = 27617

serv = socket.socket()
serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv.connect((ip,port))
while len(text) != 8000:
    w1 = random.choice(wordlist)
    w2 = random.choice(wordlist)
    w3 = random.choice(wordlist)
    token = f'{w1}-{w2}-{w3}'
    if token not in text:
        text.append(token)
        serv.send(token.encode())
        print(serv.recv(1024).decode())

serv.close()
