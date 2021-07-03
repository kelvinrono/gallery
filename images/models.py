from django.db import models

from django.db import models
import datetime as dt

class gallery(models.Model):
    title = models.CharField(max_length=55)
    category = models.CharField(max_length=30)
    image_path = models.ImageField(upload_to = 'gallery/')

