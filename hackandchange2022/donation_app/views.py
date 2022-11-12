from django.shortcuts import render
from .models import *



class General:
    def base(request):
        ctx = {
        "data" : "DATA FROM THE SERVER"
        }
        return render(request,"donation_app/base.html" , ctx)

    #loginrequired
    def streamer_analytics(request):
        user = request.user
        streamer =  Streamer.objects.filter(user = user)[0]
        st_donations = streamer.donation_set.all()

        data = []
        labels = []
        for donation in st_donations:
            data.append(donation.price)
            labels.append(donation.date_created.strftime(" %d.%m %H:%M"))

        # data = [6,3,1,8,6,3]
        # labels = ["day1", "day2","day3","day4","day5","day6"]
        ctx = {
        "data":data,
        "labels":labels,
        }
        return render(request, "donation_app/streamer_analytics.html", ctx)




# class Donation:
#     def create_donation(request):
