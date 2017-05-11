from rest_framework import serializers
from api.models import Instance, LANGUAGE_CHOICES, STYLE_CHOICES


class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        Create and return a new `Instance` instance, given the validated data.
        """
        return Instance.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Instance` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
