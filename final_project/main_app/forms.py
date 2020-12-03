from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta: 
        model = Profile
        fields = [
            'name',
            'current_city',
            'photo',
            'user'
        ]

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = [
            'title', 
            'city',
            'start_date',
            'description',
        ]   

class LivestreamForm(forms.ModelForm):

    class Meta:
        model = Livestream
        fields = [
            'artist', 
            'title', 
            'date', 
            'artist_img', 
            'description',
            'livestream_link'
        ]               

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']        

    