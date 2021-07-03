from django.db import models

from django.db import models
import datetime as dt

class Gallery(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=100)
    image_path = models.ImageField(upload_to = 'gallery/')
    pub_date = models.DateTimeField(auto_now_add=True)
    category =  models.ForeignKey('Category',on_delete=models.CASCADE)
    location =  models.ForeignKey('Location',on_delete=models.CASCADE)



    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']

    def save_image(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


