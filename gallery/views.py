from django.shortcuts import render
from uploading.models import UplaodPhoto
from .utils import generate_pdf

def main_page(request): 
    images = UplaodPhoto.objects.filter(owner=request.user)
    return render(request, 'gallery/main_page.html', {'images': images})

def generate_pdf_view(request):
    images = UplaodPhoto.objects.filter(owner=request.user)
    pdf_response = generate_pdf(images)
    return pdf_response
