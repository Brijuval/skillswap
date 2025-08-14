from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET'])
def welcome_users(request):
    return Response({"message": "Welcome to Skillswap Users API!"})


def get_users(request):
    return JsonResponse({"users": []})
