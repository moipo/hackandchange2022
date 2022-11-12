from django.contrib import admin
from .models import *
# Register your models here.

class ViewerAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Viewer._meta.fields]

class StreamerAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Streamer._meta.fields]

class DonationAdmin(admin.ModelAdmin):
    list_display = [x.name for x in Donation._meta.fields]

admin.site.register(Viewer, ViewerAdmin)
admin.site.register(Streamer, StreamerAdmin)
admin.site.register(Donation, DonationAdmin)
