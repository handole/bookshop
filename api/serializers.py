from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *

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

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['order_header', 'book', 'qty', 'total']

class OrderHeaderSerializer(serializers.ModelSerializer):
    OrderDetailHeader = OrderDetailSerializer(many=True)

    class Meta:
        model = OrderHeader
        fields = ['created_at', 'buyer', 'bank', 'bayar']

