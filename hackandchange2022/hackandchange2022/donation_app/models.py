from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Streamer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.SET_NULL)
    url = models.CharField(max_length = 400, default = "", blank = True)


class Viewer(models.Model):
    user = models.OneToOneField(User, null = True, blank = True, on_delete = models.SET_NULL)
    token = models.CharField(max_length = 300,default = "", blank = True)
    desired_url = models.CharField(max_length = 400,default = "", blank = True)


class Donation(models.Model):
    price = models.FloatField( blank = True )
    viewer = models.OneToOneField(Viewer, null = True, blank = True, on_delete = models.SET_NULL)
    streamer = models.ForeignKey(Streamer, null = True, blank = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, blank = True)
    message = models.CharField(max_length = 700, default = "", blank = True)
    region = models.CharField(max_length = 255, default = "", blank = True)
