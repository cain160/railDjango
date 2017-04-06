import socket

#UDP_IP = "50.160.250.112"
UDP_IP = "localhost"
UDP_PORT = 4851

lat = 40.7128
long = 74.0059
ID = 5908
MESSAGE = "ID=5908,185202.000,0063.9404,N,-0086.5205,W,1,ON"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)
while 1:
    long -= 4
    lat += 5
    ID += 1
    MESSAGE ="ID="+str(ID)+","+str(lat)+","+str(long)+",N,-0086.5205,W,1,ON"
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

    sock.sendto(bytes(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
    sock.close()


##ID=591,185202.000,0033.9404,N,-0084.5205,W,1,ON