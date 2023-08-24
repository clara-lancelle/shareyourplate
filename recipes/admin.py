from django.contrib import admin

from recipes.models import Recipe, Ingredient, Stage, Picture

class RecipeAdmin(admin.ModelAdmin): 
    list_display = ('name', 'picture', 'date_created', 'author', 'category')

class FkAdmin(admin.ModelAdmin):
    list_display = ('content', 'recipe') 

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, FkAdmin)
admin.site.register(Stage, FkAdmin)
admin.site.register(Picture)
