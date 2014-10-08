# Django Modules
from django.shortcuts import render

# App Modules
from accounts.models import User
from .models import Measurement


def idrate(request):
    information = User.objects.get(pk=request.user.id)
    #bpms by date
    bpms = Measurement.objects.filter(user=request.user).values_list('bpm', flat=True)
    #tips
    tips = objTip.getTip('1')
    tempTip = tips[0]
    return render(request, 'dashboard/idealrate.html', {'tip': tempTip, 'information': information, 'bpms': bpms})

def maxrate(request):
    #tips
    tips = objTip.getTip('1')
    tempTip = tips[1]
    #Max Rates by date
    maxs = objBpm.getMaxRates('1','2014-05-09 21:00:13','2014-05-09 22:00:13')
    return render(request, 'dashboard/maxrate.html', {'tip': tempTip, 'maxs': maxs})

def recovery(request):
    #Tips
    tips = objTip.getTip('1')
    tempTip = tips[2]
    #Recoveries
    #recoveries  = objBpm.getRecovery('1','2014-05-09 20:00:13','2014-05-09 23:00:13')
    return render(request, 'dashboard/recovery.html', {'tip': tempTip})
