from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import BuyerSet

router = DefaultRouter()
router.register(r'buyer', BuyerSet)

urlpatterns = router.urls