import json

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import Permission
from rest_framework import viewsets,filters
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from grh.models import Employe
from .models import *

class CouriesViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.filter()
    serializer_class = CourierSerializer
    search_fields = ['objet','referance_exp','n_enregistrement','type__name',]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter,)

    # Explicitly specify which fields the API may be ordered against
    ordering_fields = ('n_enregistrement',)
    # This will be used as the default ordering
    ordering = ('n_enregistrement',)

    def perform_create(self, serializer):
        if self.request and hasattr(self.request, "user"):
            user = self.request.user
            try:
                employe=Employe.objects.get(user=user)
                serializer.save(structure=employe.structure)
                super().perform_create(serializer)
            except:
                pass


    def list(self, request, *args, **kwargs):
        user=request.user
        empty_result=Courier.objects.none()
        if not user:
            self.queryset= empty_result
            return super().list(request, *args, **kwargs)

        if not user.has_perm('couriers.view_courier'):
            self.queryset = empty_result
            raise Exception("401")
        try:
            employe=Employe.objects.get(user=user)
            self.queryset= Courier.objects.filter( structure=employe.structure,deleted=False)
        except:
            raise Exception("cet utilisateur n'a pas d'employe correspondant !")
        return super().list(request, *args, **kwargs)

class ExpediteurViewSet(viewsets.ModelViewSet):
    queryset = Expediteur.objects.all()
    serializer_class = ExpediteurSerializer

    def list(self, request, *args, **kwargs):
        ids_param=request.query_params.get('ids')
        if ids_param:
            ids=ids_param.split(",")
            self.queryset=Expediteur.objects.filter(pk__in=ids)
        return super().list(request, *args, **kwargs)

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class TypeCourierViewSet(viewsets.ModelViewSet):
    queryset = TypeCourier.objects.all()
    serializer_class = TypeCourierSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    def list(self, request, *args, **kwargs):
        id_courier=request.query_params.get('id_parent')
        if id_courier:
            self.queryset=Attachment.objects.filter(courier=id_courier)
        return super().list(request, *args, **kwargs)
