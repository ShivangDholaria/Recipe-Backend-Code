# Generated by Django 3.2.9 on 2024-07-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_recipemodel_recipeimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipemodel',
            name='recipeImage',
        ),
    ]
