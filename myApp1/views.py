from django.shortcuts import render

# Create your views here.

from .models import Bloger
from .serializers import BlogerSerializer
from rest_framework import viewsets
class BlogerViewSet(viewsets.ModelViewSet):
    queryset = Bloger.objects.all()
    serializer_class = BlogerSerializer
