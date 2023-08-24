from django.conf import settings
from django.db import models
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage

class Picture(models.Model):
    # image = models.ImageField()
    image = CloudinaryField('image')
    caption = models.CharField(max_length=128, blank=True, verbose_name='Titre de l\'image')
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = CloudinaryImage(self.image).image(width=250, height=250, gravity="faces", crop="fill")
        # image = Image.open(self.image)
        # image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

class Recipe(models.Model):

    class Category(models.TextChoices):
        DESSERT = 'dessert', "Dessert"
        DISH = 'dish', "Plat"
        STARTER = 'starter', "Entrée"
        APERITIF = 'aperitif', "Apéritif"
        DRINK = 'drink', "Boissons"
        ELSE = 'else', "Autre"
    
    class Level(models.TextChoices):
        EASY = 'easy', 'Facile'
        AVERAGE = 'average', 'Moyen'
        DIFFICULT = 'difficult', 'Difficile'

    class Cost(models.TextChoices):
        LOW = 'low', 'Faible'
        AVERAGE = 'average', 'Moyen'
        HIGH = 'high', 'Elevé'
        
    picture = models.ForeignKey(Picture,null=True,  on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=128, verbose_name='Nom de la recette')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Description')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de création')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preparation_time = models.TimeField(verbose_name='Temps de préparation (hh:mm)')
    cooking_time = models.TimeField(verbose_name='Temps de cuisson (hh:mm)')
    category = models.fields.CharField(choices=Category.choices, max_length=10, verbose_name='Catégorie')    
    level = models.fields.CharField(choices=Level.choices, max_length=10, verbose_name='Niveau de difficulté')    
    cost = models.fields.CharField(choices=Cost.choices, max_length=10, verbose_name='Coût')    
    piece = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Combien de parts/personnes')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.name}'

class Stage(models.Model):

    # picture = models.ForeignKey(Picture, null=True, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=5000, verbose_name='Contenu')
    order = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
class Ingredient(models.Model):

    # picture = models.ForeignKey(Picture, null=True, on_delete=models.CASCADE, blank=True)
    content = models.CharField(max_length=5000, verbose_name='Contenu')
    order = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
