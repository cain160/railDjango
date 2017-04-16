# Create your views here.
from Railserve.models import Device, Position
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def devices(request):
    device_list = Device.objects.all()
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
    context = {
        'device': device,
        'path': paths
    }
    return HttpResponse(template.render(context, request))
