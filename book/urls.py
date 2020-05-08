from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from .views import BookViewset, StockViewSet

router = DefaultRouter()
router.register(r'', BookViewset, basename='book')
router.register(r'stocks', StockViewSet, basename='stocks')

urlpatterns = router.urls