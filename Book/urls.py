from django.conf.urls import url
from Book import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Book'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show/$', views.show, name='show'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^modify/$', views.modify, name='modify'),
    url(r'^modify/change$', views.complete_change, name='complete_change'),
    url(r'^show/delete$', views.delete, name='delete'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)