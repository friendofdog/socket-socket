import socket
from config import HEADERSIZE

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234)) # connect to IP address on port 1234
                                        # would not use gethostname if the
                                        # server is on different machine

while True:
    msg_full = ''
    new_msg = True

    while True:
        msg = s.recv(16)    # limit buffer size to 16 bytes; larger messages
                            # will be split into smaller packages
        msg = msg.decode('utf-8')

        if msg:
            if new_msg:
                print(f"new message length: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            msg_full += msg

            if len(msg_full)-HEADERSIZE == msglen:
                print('Full message received')
                print(msg_full[HEADERSIZE:])
                new_msg = True
                msg_full = ''
