import socket
from config import HEADERSIZE

class Server:
    def __init__(self, host=socket.gethostname(), port=1234):
        self.s = self.create_server(host, port)

    def create_server(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(5)
        return s

    def listen(self):
        clientsocket, address = self.s.accept()
        print(f"Connection from {address} established")

        text = "Welcome to the server. This is a longer message. Hello there."
        resp = make_response(text)
        clientsocket.send(bytes(resp, 'utf-8'))

def make_response(text):
    header = f"{len(text):<{HEADERSIZE}}"
    msg = f"{header}" + text
    return msg

if __name__ == '__main__':
    server = Server()
    while True:
        server.listen()
