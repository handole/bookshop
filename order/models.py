from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    nm_bank = models.CharField(max_length=50, blank=True, null=True)
    aktif = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'bank'


class OrderHeader(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orderbuyer')
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
    