import socket
from config import HEADERSIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234)) # connect to IP address on port 1234
                                        # would not use gethostname if the
                                        # server is on different machine

class Message:
    def __init__(self):
        self.content = ''
        self.len = 0
        self.isnew = True

    def handle_new_msg(self, pck):
        if self.isnew:
            print(f"new message length: {pck[:HEADERSIZE]}")
            self.len = int(pck[:HEADERSIZE])
            self.isnew = False

    def append_to_msg(self, pck):
        print('appending:', pck)
        self.content += pck

    def handle_complete_msg(self):
        if len(msg.content)-HEADERSIZE == msg.len:
            print('Full message received')
            print(msg.content[HEADERSIZE:])
            self.isnew = True
            self.content = ''

def handle_pck():
    pck = s.recv(16)    # limit buffer size to 16 bytes; larger messages
                        # will be split into smaller packages
    pck = pck.decode('utf-8')
    return pck

while True:
    msg = Message()

    while True:
        pck = handle_pck()              # receive and decode package; not part
                                        # of msg object because pck is used to
                                        # construct props, is not a prop itself

        if pck:
            msg.handle_new_msg(pck)     # set len and isnow props of msg upon
                                        # receipt of a new response

            msg.append_to_msg(pck)      # append received package to msg

            msg.handle_complete_msg()   # return full message and reset msg
                                        # props to defaults when full message
                                        # has been constructed
