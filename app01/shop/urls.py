from django.conf.urls import url

from . import views

app_name = "shop"
urlpatterns = [

    url(r'^$', views.index, name='index'),
]
