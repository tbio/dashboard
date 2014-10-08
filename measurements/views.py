# Django Modules
from django.shortcuts import render

# App Modules
from accounts.models import User
from .models import Measurement
from advices.models import Tip


def idrate(request):
    information = User.objects.get(pk=request.user.id)
    #bpms by date
    bpms = Measurement.objects.filter(user=request.user).values_list('bpm', flat=True)
    #tips
    tips = Tip.objects.all()
    return render(request, 'dashboard/idealrate.html', {'tips': tips, 'information': information, 'bpms': bpms})


def maxrate(request):
    #tips
    tips = Tip.objects.all()
    #Max Rates by date
    maxs = Measurement.objects.filter(user=request.user).values_list('hr_max', flat=True)
    return render(request, 'dashboard/maxrate.html', {'tips': tips, 'maxs': maxs})


def recovery(request):
    #Tips
    tips = Tip.objects.all()
    #Recoveries
    recoveries = Measurement.objects.filter(user=request.user).values_list('recovery', flat=True)
    return render(request, 'dashboard/recovery.html', {'tips': tips, 'recoveries': recoveries})
