from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('livestreams/', views.livestreams_index, name='livestreams_index'),
    path('signup/', views.signup, name='signup'),
    path('posts/new/', views.new_post, name='new_post'),
    path('posts/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.show_post, name='show_post'),  
    path('posts/<int:post_id>/delete_post/', views.delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),

    # path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    # path('profile/new/', views.new_profile, name='new_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('profile/<int:profile_id>/', views.user_profile, name='user_profile'),







]
