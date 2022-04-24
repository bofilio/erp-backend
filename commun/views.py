from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt import  authentication
from rest_framework.response import Response
from  commun.util import Util


class EmailAPI(APIView):
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]
    def post(self, request, format=None):
        data=request.data
        print (data)
        #try:
        Util.send_email(subject=data["subject"], message=data["message"], source=data["source"], to=data["to"] or[], cc=[],
        attachments=data["attachments"] or [])
        return Response(len(data["to"]))
        #except:
            #raise Exception({"details":"bad request"})



