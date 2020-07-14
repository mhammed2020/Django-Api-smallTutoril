from rest_framework import serializers
from .models import Bloger


class BlogerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Bloger
        fields = ('firstName','lastName','email','subject','description','created')
   