from rest_framework import serializers
from .models import *
class registrationserializer(serializers.ModelSerializer):
    class Meta:
        model = registrationModel
        fields = '__all__'