from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UplaodPhoto(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/images/', blank=False)
    description = models.TextField()
    prediction = models.CharField(max_length=110, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    