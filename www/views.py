from django.shortcuts import render, redirect


def stream(request):
    context = {}
    if request.user.is_authenticated():
        return render(request, 'dashboard/stream.html', context)
    else:
        return redirect('/signin/')
