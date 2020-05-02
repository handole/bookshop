from rest_framework import serializers
from .models import Bank, OrderDetail, OrderHeader

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ['order_header', 'book', 'qty', 'total']

class OrderHeaderSerializer(serializers.ModelSerializer):
    OrderDetailHeader = OrderDetailSerializer(many=True)

    class Meta:
        model = OrderHeader
        fields = ['created_at', 'buyer', 'bank', 'bayar']

