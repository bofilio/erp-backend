from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "is_superuser", "is_staff","email"]

class StrucutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = "__all__"

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = "__all__"