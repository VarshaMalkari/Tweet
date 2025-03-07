from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class tweet_form(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class TweetSearchForm(forms.Form):
    query = forms.CharField(
        label='Search Tweets',
        max_length=100,
        required=False,  # Allow empty search
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search tweets or users...'})
    )