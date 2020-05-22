import socket
import time
from config import HEADERSIZE

def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234)) # bind IP address on port 1234
    s.listen(5)                         # queue limit for incoming connections
    return s

def create_clientsocket():
    c, address = s.accept()     # if anyone connects, will accept these are
                                # socket and addr of client
    print(f"Connection from {address} established")
    return c

def make_header(msg):
    return f"{len(msg):<{HEADERSIZE}}"

def telltime():
    time.sleep(3)
    msg = f"The time is {time.time()}"
    header = make_header(msg)
    msg = f"{header}" + msg

    c.send(bytes(msg, 'utf-8'))

def listen():
    msg = "Welcome to the server. This is a longer message."
    header = make_header(msg)
    msg = f"{header}" + msg

    c.send(bytes(msg, 'utf-8'))

    while True:
        telltime()

s = create_server()
c = create_clientsocket()

while True:
    listen()
