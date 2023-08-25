from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory, formset_factory
from django.db.models import Q
from django.contrib import messages

from authentication.models import User
from . import forms, models
import logging

logger = logging.getLogger('django')


def search_page(request):
    query = ''
    recipes = []
    users = []
    form = forms.SearchForm()
    logging.error(request.POST)
    if request.method == "POST":
        if 'search_input' in request.POST:
            form = forms.SearchForm(request.POST)
            query = request.POST['search_input']
            recipes = models.Recipe.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
            users = User.objects.filter(username__icontains=query)
    context = {
        'form': form,
        'query': query,
        'title': 'Zone de recherche',
        'recipes': recipes,
        'users': users,
    }
    return render(request, 'recipes/search_page.html', context)

# all recipes
def recipes_all(request):
    recipes = models.Recipe.objects.all().order_by('-date_created')
    filters = models.Recipe.Category
    if recipes :
        if request.method == 'GET':
            logging.error(request.GET)
            if request.GET.get('filter'):
                request_filter = request.GET.get('filter')
                if request_filter in filters.names:
                    recipes = models.Recipe.objects.filter(category__icontains=request_filter.lower())
        paginator = Paginator(recipes, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'title': 'Toutes les recettes',
            'filters': filters,
        } 
    if not recipes :
        messages.info(request, "Oups..Aucune recette n'a été trouvée.")
        context = { 
            'filters': filters,
            'title': 'Toutes les recettes',
        }

    return render(request, 'recipes/recipes_all.html', context=context)


# recipes of followed accounts
@login_required
def home(request):
    recipes = models.Recipe.objects.filter(
                author__in=request.user.follows.all()
            ).order_by('-date_created')   
    if not recipes :
        if request.user.follows.all().count() == 0:
            messages.info(request, "Vous ne suivez aucun membres ? Voici toutes les recettes ajoutées récemment :")
        else:
            messages.info(request, "Il semble que les membres que vous suivez n'aient publié aucune recettes.. Voici toutes les recettes ajoutées récemment :")
        recipes = models.Recipe.objects.all().order_by('-date_created')
    if recipes:
        paginator = Paginator(recipes, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    else :
        page_obj = []
        messages.info(request, "Oups.. C'est bien vide ici.")
    context = {
        'page_obj': page_obj,
        'title': 'Accueil',
    }
    return render(request, 'recipes/home.html', context)

# recipes of request accounts
@login_required
def recipes_feed(request, account_id):
    recipes = models.Recipe.objects.all().filter(author=account_id).order_by('date_created')
    account = User.objects.get(id=account_id)
    filters = models.Recipe.Category
    if recipes :
        if request.method == 'GET':
            logging.error(request.GET)
            if request.GET.get('filter'):
                request_filter = request.GET.get('filter')
                if request_filter in filters.names:
                    recipes = models.Recipe.objects.filter(category__icontains=request_filter.lower()).order_by('date_created')
        paginator = Paginator(recipes, 15)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'title': f"Recettes de {account}", 
            'filters': filters,
        } 
    if not recipes :
        messages.info(request, "Oups..Aucune recette n'a été trouvée.")
        context = {
             'filters': filters,
             'title': f"Recettes de {account}", 
        }
    return render(request, 'recipes/recipes_feed.html', context=context)

    
@login_required
def recipe_create(request):
    recipe_form = forms.RecipeForm()
    picture_form = forms.PictureForm()
    StageFormSet = formset_factory(forms.StageForm, formset=forms.BaseRecipeFormSet, extra=1, max_num=15, can_delete=True)
    formset = StageFormSet()
    IngredientFormset = formset_factory(forms.IngredientForm, formset=forms.BaseRecipeFormSet, extra=1, max_num=15, can_delete=True)
    ingredient_formset = IngredientFormset(prefix='ingredient_form')
    if request.method == 'POST':
        recipe_form = forms.RecipeForm(request.POST)
        picture_form = forms.PictureForm(request.POST, request.FILES)
        formset = StageFormSet(request.POST)
        ingredient_formset = IngredientFormset(request.POST, prefix='ingredient_form')
        if all([recipe_form.is_valid(), formset.is_valid(),ingredient_formset.is_valid(), picture_form.is_valid()]):
            try:
                if picture_form.cleaned_data:
                    picture = picture_form.save()
                    if recipe_form.cleaned_data:
                        recipe = recipe_form.save(commit=False)
                        recipe.author = request.user
                        recipe.picture = picture
                        recipe.save()
                        for index, form in enumerate(formset, start=1):
                            stage = form.save(commit=False)
                            stage.recipe = recipe
                            stage.order = index
                            stage.save()  
                        for index, form in enumerate(ingredient_formset, start=1):
                            ingredient = form.save(commit=False)
                            ingredient.recipe = recipe
                            ingredient.order = index
                            ingredient.save()  
                        messages.success(request, "Super, Une nouvelle recette à été ajouté !")
                        return redirect('recipe-view', recipe.id)
            except Exception as e:
                logging.error("Exception occurred", exc_info=True)
    context = {
        'recipe_form': recipe_form,
        'picture_form': picture_form,
        'formset': formset,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'recipes/recipe_create.html', context=context)

@login_required
def recipe_view(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)
    if request.method == 'POST':
        if 'follow' in request.POST:
            action = request.POST['follow']
            if action == 'unfollow':
                request.user.follows.remove(recipe.author)
                messages.success(request, f"Vous ne suivez désormais plus { recipe.author.username } !")
            else:
                request.user.follows.add(recipe.author)
                messages.success(request, f"Vous suivez désormais { recipe.author.username } !")

            request.user.save()
            
    context = {
        'recipe': recipe,
        'title': recipe.name,
    }
    return render(request, 'recipes/recipe_view.html', context)

@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)
    picture = get_object_or_404(models.Picture, id=recipe.picture.id)
    stages = models.Stage.objects.all().filter(recipe=recipe_id)
    ingredients = models.Ingredient.objects.all().filter(recipe=recipe_id)
    recipe_form = forms.RecipeForm(instance=recipe)
    picture_form = forms.PictureForm(instance=picture)
    StageFormSet = modelformset_factory(models.Stage, forms.StageForm, formset=forms.BaseRecipeModelFormSet, can_delete=True, max_num=15)
    IngredientFormset = modelformset_factory(models.Ingredient, forms.IngredientForm, formset=forms.BaseRecipeModelFormSet, can_delete=True, max_num=15)
    formset = StageFormSet(queryset=stages)
    ingredient_formset = IngredientFormset(queryset=ingredients, prefix='ingredient_form')
    delete_form = forms.DeleteRecipeForm()
    if request.method == 'POST':
        if 'edit_recipe' in request.POST:
            recipe_form = forms.RecipeForm(request.POST, instance=recipe)
            picture_form = forms.PictureForm(request.POST, instance=picture)
            formset = StageFormSet(request.POST)
            ingredient_formset = IngredientFormset(request.POST, queryset=ingredients, prefix='ingredient_form')
            if all([recipe_form.is_valid(), formset.is_valid(), ingredient_formset.is_valid(), picture_form.is_valid()]):
                try:
                    if picture_form.cleaned_data:
                        picture = picture_form.save()
                        if recipe_form.cleaned_data: 
                            recipe = recipe_form.save(commit=False)
                            recipe.author = request.user
                            recipe.picture = picture
                            recipe.save()
                            models.Stage.objects.all().filter(recipe=recipe_id).delete()
                            for index, form in enumerate(formset, start=1):
                                if form["content"].data != '' and form["content"].data is not None:
                                    stage = form.save(commit=False)
                                    stage.recipe = recipe
                                    stage.order = index
                                    stage.save()  
                            models.Ingredient.objects.all().filter(recipe=recipe_id).delete()
                            for index, form in enumerate(ingredient_formset, start=1):
                                if form["content"].data != '' and form["content"].data is not None:
                                    ingredient = form.save(commit=False)
                                    ingredient.recipe = recipe
                                    ingredient.order = index
                                    ingredient.save()  
                            messages.success(request, "Votre recette a été modifiée !")
                            return redirect('recipe-view', recipe.id)
                except Exception as e:
                    logging.error("Exception occurred", exc_info=True)
                # return redirect('home')
        if 'delete_recipe' in request.POST:
            delete_form = forms.DeleteRecipeForm(request.POST)
            if delete_form.is_valid():
                recipe.delete()
                messages.success(request, "Recette supprimée avec succès.")
                return redirect('home')
    context = {
        'recipe_form': recipe_form,
        'picture_form': picture_form,
        'formset': formset,
        'delete_form': delete_form,
        'ingredient_formset': ingredient_formset,
    }
    return render(request, 'recipes/recipe_edit.html', context=context)
                
        
@login_required
def follow_users(request):
    unfollowed_account = User.objects.exclude(id__in=request.user.follows.all())
    if request.method == 'POST':
        if 'follow' in request.POST:
            action = request.POST['follow']
            action_user = User.objects.get(id=request.POST['user'])
            if action_user :
                if action == 'unfollow':
                    request.user.follows.remove(action_user)
                    messages.success(request, f"Vous ne suivez désormais plus { action_user } !")
                else:
                    request.user.follows.add(action_user)
                    messages.success(request, f"Vous suivez désormais { action_user } !")

            request.user.save()
    context = {
        'title': 'Follow & Followers',
        'unfollowed_account': unfollowed_account,
    }
    return render(request, 'recipes/follow_users.html', context=context)
