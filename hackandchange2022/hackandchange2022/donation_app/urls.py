from django.urls import path
from .views import *

urlpatterns = [
    path('', General.base , name = "base")
]
