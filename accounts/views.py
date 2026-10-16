from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import role_required


@login_required
def home(request):
    if not hasattr(request.user, 'profile'):
        return HttpResponse("Votre compte n'a pas de profil. Contactez l'administrateur.")
    if request.user.profile.role == 'GROSSISTE':
        return redirect('accounts:wholesaler_dashboard')
    return redirect('accounts:retailer_dashboard')


@login_required
@role_required('GROSSISTE')
def wholesaler_dashboard(request):
    return render(request, 'wholesaler/dashboard.html')


@login_required
@role_required('DETAILLANT')
def retailer_dashboard(request):
    return render(request, 'retailer/dashboard.html')