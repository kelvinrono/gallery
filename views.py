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
    tech_cetegory=Category.objects.get(pk=1)
    tech_images=Gallery.objects.filter(category=tech_cetegory)
    return render(request,'category/technology.html', {"tech_images": tech_images})
def nature(request):
    nature_category = Category.objects.get(pk=2)
    nature_images = Gallery.objects.filter(category=nature_category)
    return render(request,'category/nature.html', {"nature_images": nature_images})
def meditation(request):
    meditation_category = Category.objects.get(pk=3)
    med_images = Gallery.objects.filter(category=meditation_category)
    return render(request,'category/meditation.html',{"meditation_images": med_images})