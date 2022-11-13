from django.urls import path
from .views import *

urlpatterns = [
    path('', General.start_page , name = "start_page"),
    path('streamer/analytics/', General.streamer_analytics, name = "streamer_analytics"),
    path('streamer/get_streamer_url/', General.get_streamer_url, name = "get_streamer_url"),
    path('login/',Authorization.login , name = 'login'),
    path('register/', Registration.register, name='register'),
]
