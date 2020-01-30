from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from .models import LoginApi
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view





@api_view(['POST',])
def registration(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] : "successfully registered a new user"
            data['email'] : account.email
            data['username'] : account.username
        else:
            data = serializer.errors
        return Response(data)


