from rest_framework import routers
from django.conf.urls import url
from .views import BuyerSet

router = routers.DefaultRouter()
router.register(r'buyer', BuyerSet)