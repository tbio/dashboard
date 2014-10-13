# Django Modules
from django.shortcuts import render

# App Modules
from accounts.models import User
from .models import Measurement
from advices.models import Tip


def idrate(request):
    information = User.objects.get(pk=request.user.id)
    #bpms by date
    bpms = Measurement.objects.filter(user=request.user).values('bpm', 'date_created')
    #tips
    tips = Tip.objects.all()
    ctx = {'tips': tips, 'information': information, 'bpms': bpms}
    if tips.count() > 0:
        temptip = tips[0]
        ctx['temptip'] = temptip
    return render(request, 'dashboard/idealrate.html', ctx)


def maxrate(request):
    #tips
    tips = Tip.objects.all()
    #Max Rates by date
    maxs = Measurement.objects.filter(user=request.user).values('hr_max', 'date_created')
    ctx = {'tips': tips, 'maxs': maxs}
    if tips.count() > 0:
        temptip = tips[0]
        ctx['temptip'] = temptip
    return render(request, 'dashboard/maxrate.html', ctx)


def recovery(request):
    #Tips
    tips = Tip.objects.all()
    #Recoveries
    recoveries = Measurement.objects.filter(user=request.user).values('recovery', 'date_created')
    ctx = {'tips': tips, 'recoveries': recoveries}
    if tips.count() > 0:
        temptip = tips[0]
        ctx['temptip'] = temptip
    return render(request, 'dashboard/recovery.html', ctx)
