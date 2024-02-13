from django import forms
from .models import UploadPhoto


class UploadPhotoForm(forms.ModelForm):
    class Meta: 
        model = UploadPhoto
        fields = ['image']

