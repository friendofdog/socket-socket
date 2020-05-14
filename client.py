import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234)) # connect to IP address on port 1234
                                        # would not use gethostname if the
                                        # server is on different machine

msg_full = ''

while True:
    msg = s.recv(1024)                  # limit buffer size to 1024 bytes
                                        # larger streams of data will be split
                                        # into multiple packages

    if len(msg) > 0:
        msg_full += msg.decode('utf-8')
    else:
        break

print(msg_full)
