from rest_framework import serializers
from .models import lolvs

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = lolvs
        fields = "__all__"