from django.shortcuts import render
from .models import *



class General:
    def base(request):
        ctx = {
        "data" : "DATA FROM THE SERVER"
        }
        return render(request,"donation_app/base.html" , ctx)

    def streamer_analytics(request):
        # user = request.user
        # streamer =  Streamer.objects.filter(user = user)[0]
        # st_donations = streamer.donation_set.all()
        # ctx = {
        # "st_donations": st_donations,
        # }
        ctx = {}
        return render(request, "donation_app/streamer_analytics.html", ctx)




# class Donation:
#     def create_donation(request):
