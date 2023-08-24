# Generated by Django 4.2.2 on 2023-06-22 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Dessert', 'Dessert'), ('Plat', 'Dish'), ('Entrée', 'Starter'), ('Apéritif', 'Aperitif'), ('Boissons', 'Drink'), ('Autre', 'Else')], max_length=10, verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cost',
            field=models.CharField(choices=[('Faible', 'Low'), ('Moyen', 'Average'), ('Elevé', 'High')], max_length=10, verbose_name='Coût'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nom'),
        ),
    ]