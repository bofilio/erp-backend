from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class StructureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Structure.objects.all()
    serializer_class = StrucutureSerializer

class EmployeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer

    def retrieve(self, request, pk=None):
        pk_type = request.query_params.get('pk_type')
        if pk_type and pk_type=="user":
            employe = get_object_or_404(self.queryset, user__id=pk)
            serializer=self.serializer_class(employe)
            return Response(serializer.data)
        #else will get by employe id
        return super(request,pk)

