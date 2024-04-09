from rest_framework import serializers
from humanhealth.models import Food
from humanhealth.models import Sleep
from humanhealth.models import Water
from humanhealth.models import Walk,Location
from humanhealth.models import Mobile

class Foodserializer (serializers.ModelSerializer):
     class Meta:
          model=Food
          fields="__all__"


class Sleepserializer (serializers.ModelSerializer):
     class Meta:
          model=Sleep
          fields="__all__"

class Waterserializer (serializers.ModelSerializer):
     class Meta:
          model=Water
          fields="__all__"

class Walkserializer (serializers.ModelSerializer):
     class Meta:
          model=Walk
          fields="__all__"

class Mobileserializer (serializers.ModelSerializer):
     class Meta:
          model=Mobile
          fields="__all__"



class Locationserializer (serializers.ModelSerializer):
     class Meta:
          model=Location
          fields="__all__"