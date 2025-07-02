from django.shortcuts import render
from . models import About, Client, Projects, Service, SocialMedia, Testimonial

# Create your views here.
def home(request):
    projects = Projects.objects.all()
    about = About.objects.all()
    service = Service.objects.all()
    social_media = SocialMedia.objects.all()
    client = Client.objects.all()
    testimonial = Testimonial.objects.all()

    body = {
        'projects': projects,
        'abouts': about,
        'services': service,
        'social_medias': social_media,
        'clients': client,
        'testimonials': testimonial
    }

    return render(request, 'profil/index.html', body)

# def about(request):
#     return render(request, 'profil/index.html')
