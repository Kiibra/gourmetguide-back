from gourmetguide.models import Recipe
from gourmetguide.serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def recipes (request):
    data = Recipe.objects.all()
    serializer = RecipeSerializer(data, many=True)
    return JsonResponse({'recipes': serializer.data})

@api_view(['POST'])
def add_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Recipe added successfully!', 'recipes': serializer.data}, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def recipe_detail(request, recipeId):
    data = get_object_or_404(Recipe, id=recipeId)
    serializer = RecipeSerializer(data)
    return JsonResponse({'recipe': serializer.data}, status=201)

@api_view(['PUT'])
def recipe_update(request, recipeId):
    recipe= get_object_or_404(Recipe, id=recipeId)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Recipe updated successfully!', 'recipes': serializer.data}, status=201)
    return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def recipe_delete(request, recipeId):
    recipe = get_object_or_404(Recipe, id=recipeId)
    recipe.delete()
    return JsonResponse({'message': 'Recipe deleted successfully!'}, status=204)