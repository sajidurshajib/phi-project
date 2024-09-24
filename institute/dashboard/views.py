from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts')
def dashboard(request):
    context = {'title': 'Dashboard'}
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='/accounts')
def profile(request):
    context = {'title': 'Profile'}
    return render(request, 'dashboard/profile.html', context)

