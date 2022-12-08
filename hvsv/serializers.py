from .models import Citizen
from rest_framework import serializers


class CitizenSerializer(serialzers.ModelSerialzizer):
    class Meta:
        model = Citizen
        fields =['id', 'name', 'power', 'affiliation']

