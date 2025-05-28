from django.urls import path
from profil import views

urlpatterns = [
    path('omah/', views.home),
    path('about/', views.about),
]
