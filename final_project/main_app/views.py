from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# ----------SIGN UP

def signup(request):
    return render(request, 'accounts/signup.html')


#--------Resources Page

def resources(request):
    return render(request, 'resources.html')

#-----------Livestreams
def livestreams(request):
    return render(request, 'livestreams.html')
