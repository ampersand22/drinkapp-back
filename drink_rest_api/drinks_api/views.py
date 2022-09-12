from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import DrinkSerializer
from .models import Drink

class DrinkList(generics.ListCreateAPIView):
    queryset = Drink.objects.all().order_by('id') 
    serializer_class = DrinkSerializer 

class DrinkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drink.objects.all().order_by('id')
    serializer_class = DrinkSerializer
