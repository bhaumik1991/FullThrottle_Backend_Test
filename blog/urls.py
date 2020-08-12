from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserApi.as_view()),
    path('activityperiod/', views.ActivityPeriodApi.as_view()),
]