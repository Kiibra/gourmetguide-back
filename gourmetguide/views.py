from gourmetguide.models import Recipe
from gourmetguide.serializers import RecipeSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def recipes (request):
    data = Recipe.objects.values()
    serializer = RecipeSerializer(data, many=True)
    return JsonResponse({'recipes': serializer.data})