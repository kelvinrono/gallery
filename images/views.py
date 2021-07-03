from images.models import Gallery, Category, Location
from django.shortcuts import render


def index(request):
    
    return render(request, 'all-photos/index.html')

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'all-photos/gallery.html',{'gallery':gallery})

def image_location(request):
   
    karatina  = Location.objects.get(pk=2)
    kericho = Location.objects.get(pk=3)
 
    
    karatina_images = Gallery.objects.filter(location=karatina)
    kericho_images = Gallery.objects.filter(location=kericho)
    
    return render(request, 'all-photos/location.html', {"karatina": karatina_images,"kericho":kericho_images})