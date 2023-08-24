from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, PasswordInput
from cloudinary.forms import cl_init_js_callbacks      

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'profile_photo')
        widgets = {
        'username': TextInput(attrs={
            'class': "floating-input peer",
            'placeholder': ' ',
            }),
        'email': EmailInput(attrs={
            'class': "floating-input peer",
            'placeholder': ' ',
            }),
        }

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_photo', )
