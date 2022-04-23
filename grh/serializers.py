from rest_framework import serializers
from .models import *


class StrucutureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = "__all__"

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = "__all__"