import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.http import HttpResponse, JsonResponse


# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
    return Response(data)


@api_view(["GET"])
def products(request, *args, **kwargs):
    instance = Product.objects.all()
    serializer = ProductSerializer(instance, many=True).data
    return Response(serializer)


@api_view(["GET"])
def product_detail(request, pk):
    instance = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance, many=False).data
    return Response(serializer)


@api_view(["POST"])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def product_delete(request, pk):
    instance = Product.objects.get(id=pk)
    instance.delete()

    return HttpResponse(status=204)


@api_view(["PUT"])
def product_update(request, pk):
    instance = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
