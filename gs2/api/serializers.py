from .models import student
from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

def create(self, validate_data):
    return student.objects.create(**validate_data)