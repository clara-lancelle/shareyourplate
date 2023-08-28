from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    # profile_photo = models.ImageField(verbose_name='Photo de profil', null=True, blank=True)
    def validate_image(file):
        filesize = file.size
        megabyte_limit = 3.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("L'image est trop grande, la taille maximale est de %sMB" % str(megabyte_limit))
        
    profile_photo = CloudinaryField('Photo de profil', null=True, blank=True, validators=[validate_image])
    username = models.CharField(max_length=40, unique=True, verbose_name="Nom d'utilisateur")
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='Comptes à suivre',
        related_name='users'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
