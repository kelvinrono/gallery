from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views
urlpatterns=[
    url(r'^$', views.index, name='home'),
    url(r'gallery/', views.gallery, name='gallery'),
    url(r'location/', views.location, name='location'),
    url(r'category/', views.category, name='category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)