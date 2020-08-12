from .serializers import *
from rest_framework import generics
from .models import *

class UserApi(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class ActivityPeriodApi(generics.ListCreateAPIView):
    queryset=ActivityPeriod.objects.all()
    serializer_class=ActivityPeriodSerializer