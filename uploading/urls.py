from django.urls import path 
from .views import Uploading_Views , get_csrf_token

urlpatterns = [
    path('', Uploading_Views, name='Uploading_Views'),
    path('get-csrf-token/', get_csrf_token, name='get_csrf_token')
]