from rest_framework import serializers
from .models import jsonData

class JsonSerializer(serializers.ModelSerializer):

    class Meta:
        model = jsonData
        fields = '__all__'