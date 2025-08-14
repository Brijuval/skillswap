from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Skillswap Home!"})
from django.shortcuts import render

# Create your views here.
