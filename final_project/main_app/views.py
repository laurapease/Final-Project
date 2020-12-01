from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from .forms import PostForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
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


def logout(request):
    auth.logout(request)
    return redirect('about')

#-----------Post a Job

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.posted_by = request.user
            new_post.save()
            return redirect('show_post', post_id)
    else:
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/new.html', context)
   
def edit_post(request):
        return render(request, 'posts/edit.html')

def posts_index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/index.html', context)

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {'post': post}
    return render(request, 'posts/show.html', context)


def signup(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password == password2:
            # Check if username exists
            if User.objects.filter(username=username).exists():
                return render(request, 'registration/signup.html', {'error': 'That username has already been registered. Please try a different username'})
            else:
                # Check if email exists
                if User.objects.filter(email=email).exists():
                    return render(request, 'registration/signup.html', {'error': 'That email has already been registered'})
                else:
                    # Register User
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            return render(request, 'registration/signup.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'registration/signup.html')



# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('new_profile')
#         else: 
#             error_message = 'This username is already in use. Please try another name.'
#             form = UserCreationForm()
#             context = {'form': form, 'error_message': error_message}
#             return render(request, 'registration/signup.html',context)
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)

# @login_required
# def new_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_profile = form.save(commit=False)
#             new_profile.user = request.user
#             new_profile.save()
            
#             return redirect('user_profile', new_profile.id)
#         else:
#             return render(request, 'profile/new.html', {'form': form})
#     else: 
#         form = ProfileForm()
#         context = {'form': form}
#         return render(request, 'profile/new.html', context)



