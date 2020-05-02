from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Stock, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'category', 'cover', 'sinopsis', 'isbn', 'publication_date', 'author', 'timestamp')

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ('book_id', 'price', 'stocks', 'timestamp')
