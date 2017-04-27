'''
    Simple udp socket server
'''
import datetime
import socket
import sys

import django

django.setup()
from Railserve import models

##from Railserve.models import Position, Device

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 4851  # Arbitrary non-privileged port


def parseDate(date, time):
    h = int(time[:2])
    min = int(time[2:4])
    s = round(float(time[4:]))

    year = 2000 + int(date[4:])
    month = int(date[2:4])
    day = int(date[:2])

    formatted_date = datetime.datetime(year=year, month=month, day=day, hour=h, minute=min, second=s)

    return formatted_date

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

    id = out[0]
    time = out[2]
    latitude = out[4]
    longitude = out[6]
    speed = out[8]
    date = out[10]
    status = out[14]

    # IdToParse = out[0].split("=")
    # id = IdToParse[1]

    print(out)
    print("latitude " + latitude)
    print("longitude " + longitude)
    print("status " + status)
    #print("time " + time)
    print("id " + id)
    print()
    print()
    print("time : " + time)
    print()
    print()
    print("date : " + date)
    print()
    print()

    # ID=..,distance,lat,direc,long,direc,..,on/off
    actual_date = parseDate(date, time)
    print(actual_date)

    on_off = False
    if status == 'ON':
        on_off = True

    p = models.Position(latitude=latitude, longitude=longitude)
    p.save()
    d = models.Device(id=id, status=on_off, speed=speed, position=p, distance_on=0, date=actual_date)
    d.save()
    # d._do_update(pk_val=id,update_fields=date,values=actual_date,forced_update=True)



    # views.psave(longitude,latitude)

s.close()
