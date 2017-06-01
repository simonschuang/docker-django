from rest_framework import serializers
from devices.models import Device, LANGUAGE_CHOICES, STYLE_CHOICES


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
