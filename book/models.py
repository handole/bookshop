from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    cover = models.ImageField()
    sinopsis = models.TextField()
    isbn = models.CharField(max_length=15, unique=True, null=True, blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-publication_date']

    def __str__(self):
        return self.title

        
class Stock(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    stocks = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.book_id)