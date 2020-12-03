from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse
from datetime import date
from pyuploadcare.dj.forms import ImageField
from django.utils import timezone


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=50)

    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=50)
    current_city = models.CharField(max_length=100)
    photo = models.ImageField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    start_date = models.DateField(default=timezone.now)
    description = models.TextField(max_length=500)
    added_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title  

class Livestream(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    artist_img = models.ImageField(upload_to='images')
    description = models.TextField()
    livestream_link = models.URLField(max_length=200)

    def __str__(self):
        return self.artist 


class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    resource_link = models.URLField(max_length=200)

    def __str__(self):
        return self.title         
            