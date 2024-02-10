from django.shortcuts import render

# Create your views here.
import pika
import logging
from django.shortcuts import render, redirect
# from .forms import UploadForm  
from django.http import HttpResponse
from django.http import JsonResponse
from django.middleware.csrf import get_token
# from .logging import setup_logging
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .classify_image_model import classify_image


# setup_logging()

logger = logging.getLogger(__name__)

def get_csrf_token(request):
    return JsonResponse({'csrf_token': get_token(request)})

def get_rabbitmq_connection(message):
    connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    message = message

    channel.basic_publish(exchange='', routing_key='upload', body=message)


    print(f'sent message :{message}')

    connection.close()

    

@login_required
def Uploading_Views(request): 
    

        return render(request, 'upload_photo/uploading_page.html', {'form': form})
