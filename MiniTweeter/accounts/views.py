from rest_framework import viewsets
from .models import MyUser
from .serializers import MyUserModelSerializer


class MyUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserModelSerializer
    queryset = MyUser.objects.all().order_by('-username')
