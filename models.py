from django.db import models

class Gallery(models.Model):
    id=models.IntegerField( primary_key=True)
    title = models.CharField(max_length=55)
    description = models.TextField(max_length=100)
    image_path = models.ImageField(upload_to = 'gallery')
    pub_date = models.DateTimeField(auto_now_add=True)
    category =  models.ForeignKey('Category',on_delete=models.CASCADE)
    location =  models.ForeignKey('Location',on_delete=models.CASCADE)

    @classmethod
    def search_by_category(cls,search_term):
        image_category = cls.objects.filter(title__icontains=search_term)
        return image_category


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']

    def save_image(self):
        self.save()

    @classmethod
    def get_image(cls):
        image= cls.objects.get(pk=id)
        return image

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()


