from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UploadPhotoForm
from django.views.generic import View
from .classify_image import classify_image

@login_required
def uploading_Views(request):
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
            message = f'Top 5 predictions: {top_5_predictions}'
            return HttpResponse(message)
    else:
        form = UploadPhotoForm()
    return render(request, 'upload_photo/uploading_page.html', {'form': form})



