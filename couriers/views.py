from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class CouriesViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer

    @action(detail=False, methods=["post"])
    def sendemail(self, request):
        data=request.data
        print(data)
        return Response(1, status=status.HTTP_200_OK)

class ExpediteurViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = ExpediteurSerializer

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
    # @action(detail=False, methods=['get'], url_path=r'by_courier/(?P<id_courier>[^/.]+)')
    # def attchementByCourier(self, request,id_courier, *args, **kwargs):
    #     self.queryset=Attachment.objects.filter(courier__id=id_courier)
    #     return self.list(request,*args, **kwargs)