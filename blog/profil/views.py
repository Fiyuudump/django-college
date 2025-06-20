from django.shortcuts import render
from . models import Project

# Create your views here.
def home(request):
    project = Project.objects.first()
    return render(request, 'profil/index.html', {'project': project})

# def about(request):
#     return render(request, 'profil/index.html')
