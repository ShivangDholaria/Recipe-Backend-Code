from django import forms
from .models import RecipeModel

class RecipeForm(forms.ModelForm):
    
    #Meta class
    class Meta:
        model = RecipeModel
        fields = '__all__'