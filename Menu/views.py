from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from Menu.models import Menu

from Menu.serializers import MenuSerializer



class MenuViewset(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]