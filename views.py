from images.models import Gallery, Category, Location
from django.shortcuts import render


def index(request):
    
    return render(request, 'all-photos/index.html')

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,'all-photos/gallery.html',{'gallery':gallery})

def location(request):

   
    karatina  = Location.objects.get(pk=1)
    nairobi = Location.objects.get(pk=2)
    kericho = Location.objects.get(pk=3)

 
    karatina_images = Gallery.objects.filter(location=karatina)
    kericho_images = Gallery.objects.filter(location=kericho)
    nairobi_images = Gallery.objects.filter(location=nairobi)
    
    return render(request, 'all-photos/location.html', {"karatina": karatina_images,"kericho":kericho_images, "nairobi":nairobi_images})

def category(request):
    nature=Category.objects.get(pk=1)
    love=Category.objects.get(pk=2)
    technology = Category.objects.get(pk=3)
    

    nature= Gallery.objects.filter(category=nature)
    technology = Gallery.objects.filter(category=technology)
    love = Gallery.objects.filter(category=love)
    
    return render(request,'all-photos/category.html', {"technology": technology,"nature": nature, "love": love})

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        searched_images= Gallery.search_by_category(search_term)
        message=f"{search_term}"
        return render(request,'search.html',{"message":message,"images":searched_images})
    else:
        message = "You have not searched any images"
        return render(request,'search.html',{"message":message})




