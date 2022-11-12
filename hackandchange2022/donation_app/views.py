from django.shortcuts import render
from .models import *
from functools import reduce


class General:
    def base(request):
        ctx = {
        "data_last" : "data_last FROM THE SERVER"
        }
        return render(request,"donation_app/base.html" , ctx)

    #loginrequired
    def streamer_analytics(request):
        LAST = 8

        user = request.user
        streamer =  Streamer.objects.filter(user = user)[0]
        all_st_donations = streamer.donation_set.all()


        all_donation_prices, all_donation_dates,all_donation_strdates = [], [], []
        for donation in all_st_donations:
            all_donation_prices.append(donation.price)
            all_donation_dates.append(donation.date_created)
            all_donation_strdates.append(donation.date_created.strftime(" %d.%m %H:%M"))

        data_last = all_donation_prices[:LAST]
        labels_last = all_donation_strdates[:LAST]




        data_sum = []
        for i in range(len(all_donation_prices)):
            if i > 0: data_sum.append(all_donation_prices[i] + data_sum[i-1])
            else: data_sum.append(all_donation_prices[i] + 0)



        max_price = max(all_donation_prices)
        top_donation = Donation.objects.filter(price = max_price)[0]

        total_income = sum(all_donation_prices)

        avg_donation_price = round(total_income/len(all_donation_prices),2)

        ctx = {
        "data_last":data_last,
        "labels_last":labels_last,

        "data_sum":data_sum,
        "labels_sum":labels_last,

        "all_st_donations": all_st_donations,

        "top_donation" : top_donation,
        "total_income": int(total_income),
        "avg_donation_price":avg_donation_price,

        }
        return render(request, "donation_app/streamer_analytics.html", ctx)




# class Donation:
#     def create_donation(request):
