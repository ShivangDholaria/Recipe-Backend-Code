from django.shortcuts import render, get_list_or_404, HttpResponseRedirect
import json
from .models import *
from .serializers import RecipeSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets


# Create your views here.

# Home page
@api_view(['GET'])
def home_page(request):
    return Response({"message: Recipe Home Page"}, status=status.HTTP_200_OK)

# Get recipe API
@api_view(['GET'])
def get_recipes(request):
    """
    Retrieve all recipes from the database and return them as a JSON response.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        Response: A JSON response containing the serialized recipe data.

    Raises:
        None
    """

    recipes = RecipeModel.objects.all()

    recipeSerializer = RecipeSerializer(recipes, many=True)

    return Response(recipeSerializer.data, status=status.HTTP_200_OK)

# Get recipe by id API
@api_view(['GET'])
def get_recipes_by_id(request, pk):
    """
    Retrieve a recipe by its ID.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The ID of the recipe to retrieve.

    Returns:
        Response: The HTTP response containing the serialized recipe data.
                 If the recipe is not found, an error message is returned with a 404 status code.
    """

    try:
        recipes = RecipeModel.objects.get(pk=pk)
    except:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
    
    
    recipeSerializer = RecipeSerializer(recipes)

    return Response(recipeSerializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
# Add recipe API
def add_recipe(request):
    """
    Add a new recipe.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Response: The HTTP response object containing the serialized recipe data.

    Raises:
    - N/A
    """

    # is_ok = check_request_body(data=request.data)

    # if not is_ok[0]:
    #     return is_ok[1]

    data = json.loads(request.body)
    recipeSerializer = RecipeSerializer(data=data)
    recipeSerializer.is_valid()
    print(recipeSerializer.errors)
    recipeSerializer.save()
    
    return Response(recipeSerializer.data, status=status.HTTP_201_CREATED)


# Update recipe API
# TODO : 
#       1. Implement in frontend
#       2. Make changes for the filter process and redirection
@api_view(['POST'])
def update_recipe(request, category, name):

    is_ok = check_request_body(data=request.data)

    if not is_ok[0]:
        return is_ok[1]

    recipe = RecipeModel.objects.get(name=name, category=category)

    recipeSerializer = RecipeSerializer(recipe, data=request.data, partial=True)

    recipeSerializer.save()
    return Response(recipeSerializer.data, status=status.HTTP_200_OK)


# Delete recipe API
@api_view(['DELETE'])
def delete_recipe(request, pk):
    """
    Delete a recipe by its primary key.

    Args:
        request (HttpRequest): The HTTP request object.
        pk (int): The primary key of the recipe to be deleted.

    Returns:
        Response: A JSON response indicating the status of the deletion.
            If the recipe is found and deleted successfully, the response
            will have a status code of 200 OK and a message indicating
            successful deletion. If the recipe is not found, the response
            will have a status code of 404 NOT FOUND and an error message.
    """
    try:
        recipe = RecipeModel.objects.get(pk=pk)
    except RecipeModel.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    recipe.delete()
    return Response({"message": "Recipe deleted successfully"}, status=status.HTTP_200_OK)


def check_request_body(data):
    if not data.get('name').isalnum():
        return [False, Response({'message': 'Name must be alphanumeric'}, status=status.HTTP_406_NOT_ACCEPTABLE)]
    
    if not data.get('category') in RecipeModel.RecipeCategory.values:
        return [False, Response({'message': 'Category must be from the given list'}, status=status.HTTP_406_NOT_ACCEPTABLE)]
    
    if not data.get('prep_time').split(" ")[0].isnumeric():
        return [False, Response({'message': 'Prep time must be numeric'}, status=status.HTTP_406_NOT_ACCEPTABLE)]
