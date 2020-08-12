from rest_framework.serializers import ModelSerializer
from .models import *

class ActivityPeriodSerializer(ModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields = ['start_time','end_time',]

class UserSerializer(ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)
    class Meta:
        model=User
        fields = ['user_id','real_name','tz','activity_periods']