from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpattern=[
    url(r'^$', views.index, name='home')
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)