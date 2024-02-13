from django.urls import path 
from .views import uploading_Views

urlpatterns = [
    path('', uploading_Views, name='Uploading_Views'),
]