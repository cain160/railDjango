# Create your views here.
from django.db.models import Count, Min
from django.http import HttpResponse
from django.template import loader
from Railserve.models import Device, Position

from geopy.geocoders import Nominatim
from geopy.distance import great_circle
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

    device_list = Device.objects.raw('SELECT * FROM Railserve_device GROUP BY id')
    print(device_list)
    distances = []
    for d in device_list:
         device = Device.objects.filter(id=d.id)

         dist = aggregateDist(device)

         distances.append(dist)

    device_list = zip(device_list, distances)

    template = loader.get_template('Railserve/index.html')
    context = {
        'device_list': device_list,
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

    context = {
        'device': device,
        'path': paths,
        'distance': dist
    }
    return HttpResponse(template.render(context, request))
