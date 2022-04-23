from rest_framework import viewsets
from .serializers import *
from .models import *

class StructureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StrucutureSerializer

class EmployeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
