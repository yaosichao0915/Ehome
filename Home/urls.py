from django.conf.urls import url
from Home import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'Home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)