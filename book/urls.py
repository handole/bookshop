from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import BookViewset, StockViewSet

router = DefaultRouter()
router.register(r'', BookViewset, basename='book')
router.register(r'stock', StockViewSet, basename='stock')

urlpatterns = router.urls