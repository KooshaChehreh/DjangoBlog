from rest_framework import serializers
from models import Phone

class PhoneSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=50)
    brand = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Phone.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.model = validated_data.get('model', instance.model)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance