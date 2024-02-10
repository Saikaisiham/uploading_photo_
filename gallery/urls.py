from django.urls import path 
from .views import  main_page, generate_pdf_view

urlpatterns = [
    path('', main_page, name='main'),
    path('pdf', generate_pdf_view, name='pdf')
]