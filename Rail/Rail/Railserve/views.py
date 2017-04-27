# Create your views here.
from Railserve.models import Device, Position
from django.http import HttpResponse
from django.template import loader
from geopy.distance import vincenty


def distance(lat, long, lat2, long2):
    start = (lat, long)
    end = (lat2, long2)
    dist = vincenty(start, end).miles
    return dist

def aggregateDist(device_list):
    dist = 0
    for i in range(0,len(device_list)-1):

        dist+= distance(device_list[i].position.latitude, device_list[i].position.longitude, device_list[i+1].position.latitude, device_list[i+1].position.longitude)

    return dist

# Create your views here.
def devices(request):
    #device_list = Device.objects.annotate(recent_update = Min('date'))

    devices = Device.objects.raw('SELECT * FROM Railserve_device GROUP BY id')
    # print(device_list)
    distances = []
    for d in devices:
         device = Device.objects.filter(id=d.id)

         dist = aggregateDist(device)

         distances.append(dist)

    device_list = zip(devices, distances)

    template = loader.get_template('Railserve/index.html')
    context = {
        'device_list': device_list,
        'devices':devices
    }
    return HttpResponse(template.render(context, request))
    ##output =
    ##return HttpResponse("thank you")


def psave(long, lat):
    p = Position(latitude=lat, longitude=long)
    p.save()




def detail_device(request, deviceID):
    device = Device.objects.filter(id=deviceID)
    paths = device.values_list('position')
    template = loader.get_template('Railserve/html/details1.html')
    dist = aggregateDist(device)
    distances = []
    accum = 0
    print(paths)
    for i in range(0, len(paths)):
        if i == 0:
            distances.append(accum)
        else:
            accum += distance(device[i - 1].position.latitude, device[i - 1].position.longitude,
                              device[i].position.latitude, device[i].position.longitude)
            distances.append(accum)


    device_data = zip(device, distances)
    context = {
        'device_data': device_data,
        'device': device,
        'distance': dist
    }
    return HttpResponse(template.render(context, request))
