# Generated by Django 4.2.2 on 2023-07-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_stage_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='caption',
            field=models.CharField(blank=True, max_length=128, verbose_name="Titre de l'image"),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('dessert', 'Dessert'), ('dish', 'Plat'), ('starter', 'Entrée'), ('aperitif', 'Apéritif'), ('drink', 'Boissons'), ('else', 'Autre')], max_length=10, verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.TimeField(verbose_name='Temps de cuisson (hh:mm)'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cost',
            field=models.CharField(choices=[('low', 'Faible'), ('average', 'Moyen'), ('high', 'Elevé')], max_length=10, verbose_name='Coût'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='level',
            field=models.CharField(choices=[('easy', 'Facile'), ('average', 'Moyen'), ('difficult', 'Difficile')], max_length=10, verbose_name='Niveau de difficulté'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nom de la recette'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='preparation_time',
            field=models.TimeField(verbose_name='Temps de préparation (hh:mm)'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='content',
            field=models.CharField(max_length=5000, verbose_name='Contenu'),
        ),
    ]
