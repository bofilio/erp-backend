from rest_framework import viewsets
from .serializers import *

class CouriesViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

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
