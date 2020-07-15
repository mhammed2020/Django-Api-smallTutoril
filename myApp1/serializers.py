from rest_framework import serializers
from .models import Bloger


class BlogerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Bloger
        fields = '__all__'
   