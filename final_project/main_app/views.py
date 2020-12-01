from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied




# Create your views here.

#-------STATIC PAGES

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


#--------Resources Page

def resources(request):
    return render(request, 'resources.html')

#-----------Livestreams

def livestreams(request):
    return render(request, 'livestreams.html')

#-----------Post a Job

@login_required
def new_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.city_id = city_id
            new_post.save()
            return redirect('posts_index')
    else: 
        form = PostForm()
        context = {'form': form }
        return render(request, 'posts/new.html', context)

def edit_post(request):
        return render(request, 'posts/edit.html')

def posts_index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else: 
            error_message = 'This username is already in use. Please try another name.'
            form = UserCreationForm()
            context = {'form': form, 'error_message': error_message}
            return render(request, 'registration/signup.html',context)
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            
            return redirect('user_profile', new_profile.id)
        else:
            return render(request, 'profile/new.html', {'form': form})
    else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profile/new.html', context)



