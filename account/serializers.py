from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Buyer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 6,
                'max_length': 100
            },
            'email': {
                'validators': [UniqueValidator(queryset=User.objects.all())]
            }
        }

class BuyerSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='Buyer.address')
    phone = serializers.CharField(source='Buyer.phone')

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'address', 'phone')