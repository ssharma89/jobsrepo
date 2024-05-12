from django.contrib import admin
from testapp.models import HydJobs, BangJobs, PuneJobs
# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    last_display = ['date','company','title','elgibility','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)


class PuneJobsAdmin(admin.ModelAdmin):
    last_display = ['date','company','title','elgibility','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)


class BangJobsAdmin(admin.ModelAdmin):
    last_display = ['date','company','title','elgibility','address','email','phonenumber']
admin.site.register(BangJobs,BangJobsAdmin)
