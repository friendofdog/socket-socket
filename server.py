import socket

def setup():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234)) # bind IP address on port 1234
    s.listen(5)                         # queue limit for incoming connections
    return s

def listen(s):
    clientsocket, address = s.accept()  # if anyone connects, will accept
                                        # these are socket and addr of client
    print(f"Connection from {address} established")
    clientsocket.send(bytes("Welcome to the server", 'utf-8'))
    clientsocket.close()

server = setup()

while True:
    listen(server)
