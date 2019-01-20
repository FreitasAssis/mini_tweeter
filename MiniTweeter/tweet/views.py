from rest_framework import viewsets
from .models import Tweet
from .serializers import TweetModelSerializer


class TweetModelViewSet(viewsets.ModelViewSet):
    serializer_class = TweetModelSerializer
    queryset = Tweet.objects.all()
