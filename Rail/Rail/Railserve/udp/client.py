'''
    udp socket client
    Silver Moon
'''

import socket  # for sockets
import sys  # for exit

from pip._vendor.distlib.compat import raw_input

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

# host = '50.160.250.112'
host = 'localhost'
port = 4851

while (1):
    msg = raw_input('Enter message to send : ')

    try:
        # Set the whole string
        s.sendto(bytes(msg, 'utf8'), (host, port))

        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]

        print('Server reply : ' + reply.decode('utf-8'))

    except socket.error as msg:
        print('Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()
