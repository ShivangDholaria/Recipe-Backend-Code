# Generated by Django 3.2.9 on 2024-07-17 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20240716_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipemodel',
            name='category',
            field=models.CharField(blank=True, choices=[('Taiwanese Recipes', 'Taiwanese Recipes'), ('Szechuan Recipes', 'Szechuan Recipes'), ('Indian Recipes', 'Indian Recipes'), ('Thai Recipes', 'Thai Recipes'), ('Korean Recipes', 'Korean Recipes'), ('Cantonese Recipes', 'Cantonese Recipes'), ('Japanese Recipes', 'Japanese Recipes')], max_length=50),
        ),
    ]
