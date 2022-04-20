from django.urls import path, include

from .views import EmailAPI



# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('sendmail', EmailAPI.as_view()),
]