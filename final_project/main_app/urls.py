from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('signup/', views.signup, name='signup'),
    path('livestreams/', views.livestreams, name='livestreams'),



]
