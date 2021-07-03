from django.db import models

from django.db import models
import datetime as dt

class gallery(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=100)
    image_path = models.ImageField(upload_to = 'gallery/')
    # category =  models.ForeignKey('Editor',on_delete=models.CASCADE)
    # location = models.
    

