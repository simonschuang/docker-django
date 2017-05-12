from rest_framework import serializers
from instances.models import Instance, LANGUAGE_CHOICES, STYLE_CHOICES


class InstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
