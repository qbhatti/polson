from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index_view(request):
	print(request.user.username)
	return render(request, 'polsonpark/index.html', {})

def reservation_view(request):
	return render(request, 'polsonpark/reservations.html', {})

def interiors_view(request):
	return render(request, 'polsonpark/interiors.html', {})

def packages_view(request):
	return render(request, 'polsonpark/packages.html', {})

def areaguide_view(request):
	return render(request, 'polsonpark/areaguide.html', {})

def contactus_view(request):
	return render(request, 'polsonpark/contactus.html', {})