from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'couriers',CouriesViewSet)
router.register(r'classifications',ClassificationViewSet)
router.register(r'status',StatusViewSet)
router.register(r'expediteurs',ExpediteurViewSet)
router.register(r'types_couriers',TypeCourierViewSet)
router.register(r'attachments',AttachmentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]