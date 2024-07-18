from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class RecipeModel(models.Model):

    #Enum for recipe category
    class RecipeCategory(models.TextChoices):
        TAIWANESE_RECIPES = 'Taiwanese Recipe', _('Taiwanese Recipe')
        SZECHUAN_RECIPES = 'Szechuan Recipe', _('Szechuan Recipe')
        INDIAN_RECIPES = 'Indian Recipe', _('Indian Recipe')
        THAI_RECIPES = 'Thai Recipe', _('Thai Recipe')
        KOREAN_RECIPES = 'Korean Recipe', _('Korean Recipe')
        CANTONESE_RECIPES = 'Cantonese Recipe', _('Cantonese Recipe')
        JAPANE_RECIPES = 'Japanese Recipe', _('Japanese Recipe')

    #Fields
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=RecipeCategory.choices, blank=True)
    description = models.TextField()
    ingredients = models.TextField()
    procedure = models.TextField()
    # prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    # servings = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipeImage = models.TextField(blank=True)

    def __str__(self):
        return self.title

