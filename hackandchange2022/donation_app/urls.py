from django.urls import path
from .views import *

urlpatterns = [
    path('', General.base , name = "base"),
    path('streamer/analytics', General.streamer_analytics, name = "streamer_analytics")
]
