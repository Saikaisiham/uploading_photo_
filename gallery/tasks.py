from celery import Celery
from uploading.models import UplaodPhoto
from django.contrib.auth.models import User  
from .utils import generate_pdf

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost//')

@app.task
def generate_pdf_task(user_id):
    user = User.objects.get(id=user_id)
    images = UplaodPhoto.objects.filter(owner=user)
    pdf_response = generate_pdf(images)
    return pdf_response
