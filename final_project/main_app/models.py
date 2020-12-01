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
    photo = models.ImageField(upload_to='main_app/static/images', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    added_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title  


            