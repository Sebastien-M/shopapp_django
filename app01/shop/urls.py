from django.conf.urls import url

from . import views

app_name = "shop"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new$', views.PpView.as_view(), name='new'),
    url(r'^(?P<priceplan_id>[0-9]+)/infos/$', views.info, name='infos'),
    url(r'^(?P<order_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^orders$', views.OrderView.as_view(), name='orders'),
]
