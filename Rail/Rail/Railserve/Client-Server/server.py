'''
this is a test
Simple udp socket server

'''
import socket
import sys
import sqlite3

conn = sqlite3.connect('../../db.sqlite3')
cur = conn.cursor()

HOST = '192.168.1.187'  # Symbolic name meaning all available interfaces
PORT = 4850 

# Datagram (udp) socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created')
except socket.error as msg:
    print('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

# Bind socket to local host and port
try:
    print('Binding on ' + HOST + ':' + str(PORT) + '...')
    s.bind((HOST, PORT))
    print('Bound successfully...')
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# now keep talking with the client
while 1:
    data, addr = s.recvfrom(1024)
    print("Receive data from: " + str(addr))
    if not data:
        break
    
    toProcess = data.decode('utf-8')
    print(toProcess)
    reply = 'OK...' + toProcess

    out = toProcess.split(',')
    print(out)
    id, time, latitude, longitude, speedInKnots, date, validData, powerState = out[0], (str(out[2])[0:2] + ":" + str(out[2])[2:4] + ":" + str(out[2])[4:]), (out[4]+ " " + out[5]), (out[6] + " " + out[7]), out[8], ("20" + str(out[10])[4:] + "-" + str(out[10])[2:4] + "-" + str(out[10])[0:2]), out[3], out[14] 
    dateTime = date + " " + time
    print(id)
    print(time)
    print(latitude)
    print(longitude)
    print(type(speedInKnots))
    print(speedInKnots)
    print(date)
    print(validData)
    print(dateTime)
    print(powerState)
    cur.execute("INSERT INTO Railserve_device VALUES(0, 0, ?, 5, ?, ?)", (speedInKnots, dateTime, id))
    conn.commit()

s.close()
