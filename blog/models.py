from django.db import models
from datetime import datetime

class User(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    real_name = models.CharField(max_length=150)
    tz = models.CharField(max_length=150)

    def __str__(self):
        return self.user_id


class ActivityPeriod(models.Model):
    activity_id = models.ForeignKey(on_delete=models.CASCADE, to="User", related_name='activity_periods')
    start_time = models.DateTimeField(default=datetime.now, blank=False)
    end_time = models.DateTimeField(default=datetime.now, blank=False)






