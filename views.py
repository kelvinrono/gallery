from images.models import Gallery, Category, Location
from django.shortcuts import render


def index(request):
    
    return render(request, 'all-photos/index.html')

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'all-photos/gallery.html',{'gallery':gallery})

def location(request):

   
    karatina  = Location.objects.get(pk=2)
    kericho = Location.objects.get(pk=3)
 
    karatina_images = Gallery.objects.filter(location=karatina)
    kericho_images = Gallery.objects.filter(location=kericho)
    
    return render(request, 'all-photos/location.html', {"karatina": karatina_images,"kericho":kericho_images})

def category(request):
    technology=Category.objects.get(pk=1)
    nature = Category.objects.get(pk=2)
    travel = Category.objects.get(pk=3)
    music = Category.objects.get(pk=4)

    nature= Gallery.objects.filter(category=nature)
    technology = Gallery.objects.filter(category=technology)
    
    return render(request,'all-photos/category.html', {"tech_images": technology}, {"nature": nature}, {"travel": travel},{"music": music})
