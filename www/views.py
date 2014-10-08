from django.shortcuts import render


def stream(request):
    context = {}
    return render(request, 'dashboard/stream.html', context)
