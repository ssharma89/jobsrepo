from django.shortcuts import render

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')
from testapp.models import HydJobs
def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})
from testapp.models import BangJobs
def bangjobs_view(request):
    jobs_list = BangJobs.objects.all()
    return render(request, 'testapp/bangjobs.html',{'jobs_list':jobs_list})
from testapp.models import PuneJobs
def punejobs_view(request):
    jobs_list = PuneJobs.objects.all()
    return render(request, 'testapp/punejobs.html',{'jobs_list':jobs_list})
