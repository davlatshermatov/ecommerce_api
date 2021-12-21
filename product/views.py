from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product


# Create your views here.
class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:20]
        data = ProductSerializer(products, many=True).data
        return Response(data)
