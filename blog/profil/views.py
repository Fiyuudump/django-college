from django.shortcuts import render
from . models import Projects

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    return render(request, 'profil/index.html', {'projects': projects})

# def about(request):
#     return render(request, 'profil/index.html')
