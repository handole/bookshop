from rest_framework import routers
from django.conf.urls import url
from .views import BookViewset, StockViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewset)
router.register(r'stock', StockViewSet)