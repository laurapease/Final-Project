from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
import datetime


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
    photo = models.ImageField(upload_to='images', blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Posts(models.Model):
    title = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pay = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.title       