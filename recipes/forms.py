from django import forms
from django.contrib.auth import get_user_model
from django.forms import TextInput, TimeInput, Select, FileInput, SelectMultiple, NumberInput, CheckboxInput

from . import models

User = get_user_model()

class SearchForm(forms.Form):
    search_input = forms.CharField(max_length=60, label='Mot clef (nom d\'utilisateur, titre de recettes, ..)', widget=forms.TextInput(attrs={'class': "floating-input floating-input--lessmt peer",'placeholder': ' ',}))

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']
        widgets = {
            'follows': SelectMultiple(attrs={
                'class': "floating-input floating-input  peer", 
                'placeholder': ' ',
                }),
        }

class PictureForm(forms.ModelForm):
   class Meta:
        model = models.Picture
        fields = ['image', 'caption']
        widgets = {
        'caption': TextInput(attrs={
            'class': "floating-input peer",
            'placeholder': ' ',
            }),
        'image': FileInput(attrs={
            'class': "hidden input-image",
            }),
        }

class RecipeForm(forms.ModelForm):
    edit_recipe = forms.BooleanField(widget=forms.HiddenInput, initial=True,required=False)
    class Meta:
        model = models.Recipe
        exclude = ('date_created','author', 'picture')
        widgets = {
        'name': TextInput(attrs={
            'class': "floating-input peer",
            'placeholder': ' ',
            }),
        'description': TextInput(attrs={
            'class': "floating-input peer", 
            'placeholder': ' ',
            }),
        'preparation_time': TimeInput(attrs={
            'class': "floating-input peer max-w-xs", 
            'placeholder': ' ',
            'type': 'time', 
            }, format='%H:%M'),
        'cooking_time': TimeInput(attrs={
            'class': "floating-input peer max-w-xs", 
            'placeholder': ' ',
            'type': 'time', 
            }, format='%H:%M'),
        'piece': NumberInput(attrs={
            'class': "floating-input floating-input peer", 
            'placeholder': ' ',
            }),
        'category': Select(attrs={
            'class': "floating-input floating-input peer", 
            'placeholder': ' ',
            }),
        'level': Select(attrs={
            'class': "floating-input floating-input peer", 
            'placeholder': ' ',
            }),
        'cost': Select(attrs={
            'class': "floating-input floating-input peer", 
            'placeholder': ' ',
            }), 
        }

class StageForm(forms.ModelForm):
    class Meta:
        model = models.Stage
        fields = ['content']
        widgets = {
            'content': TextInput(attrs={
                'class': "floating-input floating-input--textarea peer",
                'placeholder': ' ',
            }),
        }
class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = ['content']
        widgets = {
            'content': TextInput(attrs={
                'class': "floating-input floating-input--textarea peer",
                'placeholder': ' ',
            }),
        }

class BaseRecipeModelFormSet(forms.BaseModelFormSet):
     def get_deletion_widget(self):
        return CheckboxInput(attrs={"class": "formset__delete-box"})
      
class BaseRecipeFormSet(forms.BaseFormSet):
     def get_deletion_widget(self):
        return CheckboxInput(attrs={"class": "formset__delete-box"})
      
class DeleteRecipeForm(forms.Form):
    delete_recipe = forms.BooleanField(widget=forms.HiddenInput, initial=True)
