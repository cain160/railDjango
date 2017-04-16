'''
    Simple udp socket server
'''
import socket
import sys

# from Railserve.models import Position


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 4851  # Arbitrary non-privileged port

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# now keep talking with the client
while 1:
    # receive data from client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]  ##address where the data comes from.

    if not data:
        break

    toProcess = data.decode('utf-8')
    reply = 'OK...' + toProcess

    out = toProcess.split(',')

    latitude = out[2]
    longitude = out[4]
    status = out[7]
    time = out[1]

    IdToParse = out[0].split("=")
    id = IdToParse[1]

    print(out)
    print("latitude " + latitude)
    print("longitude " + longitude)
    print("status " + status)
    print("time " + time)
    print("id " + id)

    # p = Position(latitude=latitude,longitude=longitude)
    # p.save()

    # views.psave(longitude,latitude)

s.close()
