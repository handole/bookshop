from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session

# Create your models here.
class User(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)

class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyer')
    address = models.TextField()
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.user)


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


class Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    nm_bank = models.CharField(max_length=50, blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'bank'


# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='card_books')
#     session = models.ForeignKey(Session, null=True, one_delete=models.CASCADE, related_name='cart_books')
#     book = models.ForeignKey(Stock)
#     qty = models.PositiveIntegerField()

#     def __str__(self):
#         return '{} book(s) of {}'.format(self.qty, self.book)


class OrderHeader(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyers')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='banks')
    bayar = models.IntegerField()
        
    def __str__(self):
        return str(self.buyer)


class OrderDetail(models.Model):
    order_header = models.ForeignKey(OrderHeader, on_delete=models.DO_NOTHING, related_name='OrderDetailHeader')
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, related_name='OrderDetailBooks')
    qty = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return str(self.order_header)
    
