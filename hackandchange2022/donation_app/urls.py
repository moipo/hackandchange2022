from django.urls import path
from .views import *

urlpatterns = [
    path('', General.start_page , name = "start_page"),
    path('streamer/analytics/', General.streamer_analytics, name = "streamer_analytics"),
    path('streamer/get_streamer_url/', General.get_streamer_url, name = "get_streamer_url"),
    path('streamer/streamer_url/<int:user_id>', General.streamer_url, name = "streamer_url"),
    path('streamer/profile/', General.streamer_profile, name = "streamer_profile"),
    path('login/',Authorization.login , name = 'login'),
    path('register/', Registration.register, name='register'),
]
