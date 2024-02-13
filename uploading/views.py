import pika
import logging
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UploadPhotoForm
from django.views.generic import View
from .classify_image import classify_image


def get_rabbitmq_connection(message):
    try:
        connection_parameters = pika.ConnectionParameters('127.0.0.1')
        connection = pika.BlockingConnection(connection_parameters)
        channel = connection.channel()
        message = message
        channel.basic_publish(exchange='', routing_key='upload', body=message)
        print(f'sent message :{message}')
        connection.close()
    except pika.exceptions.AMQPConnectionError as e:
        print(f'Error connecting to RabbitMQ: {e}')

@login_required
def uploading_Views(request):
    get_rabbitmq_connection('Uploading the image')
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            predictions = classify_image(image)
            top_5_predictions = predictions
            uploading = form.save(commit=False)
            uploading.owner = request.user
            uploading.prediction = top_5_predictions
            uploading.save()
            message = f'Top 5 predictions: {top_5_predictions}, rabbitmq'
            return HttpResponse(message)
    else:
        form = UploadPhotoForm()
    return render(request, 'upload_photo/uploading_page.html', {'form': form})



