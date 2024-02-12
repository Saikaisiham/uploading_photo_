from django.shortcuts import render
from uploading.models import UplaodPhoto
from django.contrib.auth.decorators import login_required
from .tasks import generate_pdf_task

def main_page(request): 
    images = UplaodPhoto.objects.filter(owner=request.user)
    return render(request, 'gallery/main_page.html', {'images': images})



@login_required
def generate_pdf_view(request):
    generate_pdf_task.delay(request.user.id)