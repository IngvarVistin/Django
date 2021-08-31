from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter the user name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Enter your password'}))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-control py-4', 'placeholder': "Enter the user name"}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-controll py-4', 'placeholder': "Enter your email address"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-controll py-4', 'placeholder': "Enter a name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-controll py-4', 'placeholder': "Enter your last name"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-controll py-4', 'placeholder': "Enter your password"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'from-controll py-4', 'placeholder': "Confirm your password"}))


    class Meta:
        model = User
        field = ('username', 'email', 'first_name', 'last-name', 'password1', 'password2')

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'from-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'from-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'from-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'from-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')