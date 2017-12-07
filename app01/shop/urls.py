from django.conf.urls import url

from . import views

app_name = "shop"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<priceplan_id>[0-9]+)infos/$', views.infos, name='infos'),
    url(r'^(?P<order_id>[0-9]+)save/$', views.save, name='save'),
    url(r'^orders$', views.orders, name='orders'),
]
