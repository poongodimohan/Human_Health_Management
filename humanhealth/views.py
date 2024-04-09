from rest_framework import viewsets
from humanhealth.models import Food
from humanhealth.serializers import Foodserializer

from humanhealth.models import Sleep
from humanhealth.serializers import Sleepserializer

from humanhealth.models import Water
from humanhealth.serializers import Waterserializer

from humanhealth.models import Walk
from humanhealth.serializers import Walkserializer

from humanhealth.models import Mobile
from humanhealth.serializers import Mobileserializer

from humanhealth.models import Location
from humanhealth.serializers import Locationserializer

# Create your views here.

def food(request):
    pass

class Foodview(viewsets.ModelViewSet):
    queryset= Food.objects.all()
    serializer_class=Foodserializer
    http_method_names=["get","post","put","delete"]



def sleep(request):
    pass

class Sleepview(viewsets.ModelViewSet):
    queryset=Sleep.objects.all()
    serializer_class=Sleepserializer
    http_method_names=["get","post","put","delete"]

def water(request):
    pass

class Waterview(viewsets.ModelViewSet):
    queryset=Water.objects.all()
    serializer_class=Waterserializer
    http_method_names=["get","post","put","delete"]


def walk(request):
    pass

class WalkView(viewsets.ModelViewSet):
    queryset=Walk.objects.all()
    serializer_class = Walkserializer
    http_method_names = ["get", "post", "put", "delete"]


def Mobileusage(request):
    pass

class Mobileview(viewsets.ModelViewSet):
    queryset=Mobile.objects.all()
    serializer_class=Mobileserializer
    http_method_names = ["get", "post", "put", "delete"]


def Location(request):
    pass

class LocationView(viewsets.ModelViewSet):
    queryset=Walk.objects.all()
    serializer_class = Locationserializer
    http_method_names = ["get", "post", "put", "delete"]

