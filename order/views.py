from django.shortcuts import render
from rest_framework import viewsets
from .models import Bank, OrderHeader, OrderDetail
from .serializers import BankSerializer, OrderDetailSerializer, OrderHeaderSerializer

# Create your views here.
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

class OrderHeaderViewSet(viewsets.ModelViewSet):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer