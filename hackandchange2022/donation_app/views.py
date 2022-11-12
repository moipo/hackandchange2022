from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from .models import *



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

        data_last = all_donation_prices[-LAST:]
        labels_last = all_donation_strdates[-LAST:]




        data_sum = []
        for i in range(len(all_donation_prices)):
            if i > 0: data_sum.append(all_donation_prices[i] + data_sum[i-1])
            else: data_sum.append(all_donation_prices[i] + 0)



        max_price = max(all_donation_prices)
        top_donation = Donation.objects.filter(price = max_price)[0]

        total_income = sum(all_donation_prices)
        total_donation_count = len(all_donation_prices)

        avg_donation_price = round(total_income/total_donation_count,2)

        ctx = {
        "data_last":data_last,
        "labels_last":labels_last,

        "data_sum":data_sum,
        "labels_sum":list(range(len(data_sum))),

        "all_st_donations": all_st_donations,

        "top_donation" : top_donation,
        "total_income": int(total_income),
        "avg_donation_price":avg_donation_price,
        "total_donation_count":total_donation_count,

        }
        return render(request, "donation_app/streamer_analytics.html", ctx)




class Authorization:
    def login(request):
        form = UserLoginForm(request.POST or None)
        ctx = {"form":form}
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username = username, password = password)
            if user is None:
                messages.add_message(request,messages.INFO,"Неверный логин и/или пароль")
                return render(request,"donation_app/signin_signup/login.html",ctx)
            else:
                print("WORKED")
                login(request,user)
                return render(request,"donation_app/streamer_analytics.html",ctx)

        return render(request,"donation_app/signin_signup/login.html",ctx)



class Registration:
    def register(request):
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            if user_form.is_valid():

                new_user = user_form.save(commit=False)

                new_user.set_password(user_form.cleaned_data['password'])

                new_user.save()
                return render(request, "donation_app/streamer_profile.html", {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request, "donation_app/signin_signup/register.html", {'user_form': user_form})
