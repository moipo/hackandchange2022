from django.shortcuts import render




class General:
    def base(request):
        ctx = {
        "data" : "DATA FROM THE SERVER"
        }
        return render(request,"donation_app/index.html" , ctx)
