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
        return JsonResponse({'message': 'Recipe added successfully!', 'recipe': serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def recipe_detail(request, recipeId):
    data = get_object_or_404(Recipe, id=recipeId)
    serializer = RecipeSerializer(data)
    return JsonResponse({'recipe': serializer.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
def recipe_update(request, recipeId):
    recipe= get_object_or_404(Recipe, id=recipeId)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'message': 'Recipe updated successfully!', 'recipe': serializer.data}, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=400)