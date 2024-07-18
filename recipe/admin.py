from django.contrib import admin
from .models import RecipeModel

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    admin.site.register(RecipeModel)