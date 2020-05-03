from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import BankViewSet, OrderHeaderViewSet, OrderDetailViewSet

router = DefaultRouter()
router.register(r'bank', BankViewSet, basename='bank')
router.register(r'orderdetail', OrderDetailViewSet, basename='orderdetail')
router.register(r'orderheader', OrderHeaderViewSet, basename='orderheader')

urlpatterns = router.urls