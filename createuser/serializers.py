from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Contact

class ContactSerializer(ModelSerializer):
    
    class Meta:
        model=Contact
        fields=['username', 'address', 'pincode', 'mobile']

    def validate(self, attrs):
        if Contact.objects.filter(username = attrs['username']).exists():
            raise serializers.ValidationError(
                {'username',('Username is already in Use')})
        return super().validate(attrs)

    # def create(self, validated_data):
    #     return Contact.objects.create(validated_data)