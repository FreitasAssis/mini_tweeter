from django.urls import path, include
from rest_framework import routers
from .views import TweetModelViewSet

router = routers.DefaultRouter()
router.register('', TweetModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
