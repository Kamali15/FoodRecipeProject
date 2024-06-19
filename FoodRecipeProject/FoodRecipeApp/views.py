from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.exceptions import ValidationError 
from .models import FoodReceipe
from .serializers import ReceipeSerializer
from rest_framework.views import APIView
from rest_framework.response import  Response




class ReceipeApi(generics.ListCreateAPIView):
    queryset = FoodReceipe.objects.all() 
    serializer_class = ReceipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category']
    # template_name = "recipe-list.html"
    def get_api(self):
        queryset = super().get_api()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def post(self, serializer):
        name = serializer.validated_data.get('name')
        if FoodReceipe.objects.filter(name = name).exists():
            raise ValidationError("This recipe is exists.")
        serializer.save()

class ReceipeModifyApi(generics.UpdateAPIView):
    queryset = FoodReceipe.objects.all()
    serializer_class = ReceipeSerializer

    def put(self, serializer):
        name = serializer.validated_data.get('name')
        if FoodReceipe.objects.filter(name=name).exclude(pk=self.get_object().pk).exists():
            raise ValidationError("This recipe name already exists.")
        serializer.save()
