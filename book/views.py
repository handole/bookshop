from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Book, Stock
from .serializers import BookSerializer, StockSerializer

# Create your views here.
class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

