from django.conf.urls import url

from shop.models import PricePlan
from . import views

app_name = "shop"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new$', views.PpView.as_view(), name='new'),
    url(r'^(?P<pk>[0-9]+)/infos/$', views.InfoView.as_view(), name='infos'),
    url(r'^(?P<order_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^orders$', views.OrderView.as_view(), name='orders'),
]
