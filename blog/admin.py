from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','real_name','tz']

class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ['activity_id','start_time','end_time']

admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
admin.site.register(User, UserAdmin)