from django.shortcuts import render
from uploading.models import UploadPhoto
from django.contrib.auth.decorators import login_required
from .tasks import generate_pdf_task


@login_required
def main_page(request): 
    images = UploadPhoto.objects.filter(owner=request.user)
    return render(request, 'gallery/main_page.html', {'images': images})



@login_required
def generate_pdf_view(request):
    generate_pdf_task.delay()