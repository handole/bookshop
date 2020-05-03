# from .models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Buyer, User
from .serializers import UserSerializer, BuyerSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BuyerSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer     