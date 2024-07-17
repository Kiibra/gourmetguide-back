from gourmetguide.models import Recipe
from gourmetguide.serializers import RecipeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse


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
        return JsonResponse({'message': 'Recipe added successfully!', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)