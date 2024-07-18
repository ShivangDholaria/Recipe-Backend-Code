from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views

# router = DefaultRouter()

# router.register(r'recipes', views.RecipeViewSet, basename='recipes')


urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('add_recipe', views.add_recipe, name='add-recipe'),
    path('get_recipes', views.get_recipes, name='get-recipe'),
    path('get_recipes_by_id/<int:pk>', views.get_recipes_by_id, name='get-recipe-by-id'),
    # path('update_recipe/', views.update_recipe, name='update-recipe'),
    path('delete_recipe/<int:pk>', views.delete_recipe, name='delete-recipe'),
]

# urlpatterns += router.urls