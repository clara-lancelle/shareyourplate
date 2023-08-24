from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms
import logging

logger = logging.getLogger('django')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "Votre mot de passe a été mis à jour.")
            return redirect('/home/')
        return super().dispatch(request, *args, **kwargs)

class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, "Vous avez été déconnecté avec succès, à très vite !")
        return super().dispatch(request, *args, **kwargs)

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})

@login_required
def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre photo de profil a été mise à jour.")
            return redirect('home')
    context = {
        'form': form,
        'title': 'Mise à jour de votre photo de profil',
    }
    return render(request, 'authentication/upload_profile_photo.html', context=context)
