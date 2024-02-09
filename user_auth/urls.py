from django.urls import path 
from .views import register_request, login_request, logout_request

urlpatterns = [
    path('', register_request, name='register'),
    path('login/', logout_request, name='login'),
    path('logout/', logout_request, name='logout')
]