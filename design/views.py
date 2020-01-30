from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .serializers import UserSerializer,ProductTypeSerializer,ProductSerializer, OrderSerializer,DesignSerializer
from .models import User , ProductType, Product, Order,Design
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.

@csrf_exempt
@permission_classes((IsAuthenticated,))
def index(request):

    #crud operation for Product modelclass
    if request.method == "GET":
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method  == "POST":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
    elif request.method == "PUT":
        try:
            product_list = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            product_list = Product.objects.get(id=id)
            product_list.delete()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#crud operation for Design modelclass
    if request.method == "GET":
        design = Design.objects.all()
        serializer = ProductSerializer(design,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method  == "POST":
        data = JSONParser().parse(request)
        serializer = DesignSerializer(data=data)
    elif request.method == "PUT":
        try:
            design = Design.objects.get(id=id)
        except Design.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        serializer = DesignSerializer(product_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            design = Design.objects.get(id=id)
            design.delete()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except Design.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#crud operation for producttypes modelclass
    if request.method == "GET":
        product_type = ProductType.objects.all()
        serializer = ProductTypeSerializer(product_type,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method  == "POST":
        data = JSONParser().parse(request)
        serializer = ProductTypeSerializer(data=data)
    elif request.method == "PUT":
        try:
            product_type = ProductType.objects.get(id=id)
        except ProductType.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        serializer = ProductTypeSerializer(product_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            product_type = ProductType.objects.get(id=id)
            product_type.delete()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except ProductType.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#crud operation for Order modelclass

    if request.method == "GET":
        order = Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method  == "POST":
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
    elif request.method == "PUT":
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        serializer = OrderSerializer(product_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            order = Order.objects.get(id=id)
            order.delete()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except Order.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#crud operation for User modelclass
    if request.method == "GET":
        user = User.objects.all()
        serializer = UserSerializer(order,many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method  == "POST":
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
    elif request.method == "PUT":
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data , status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            user.delete()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
