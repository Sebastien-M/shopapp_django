from django.conf.urls import url

from . import views

app_name = "shop"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^new$', views.PpView.as_view(), name='new'),
    url(r'^(?P<priceplan_id>[0-9]+)/infos/$', views.info, name='infos'),
    url(r'^(?P<order_id>[0-9]+)/save/$', views.save, name='save'),
    url(r'^customers$', views.OrderView.as_view(), name='orders'),
    url(r'^customers/id=(?P<customer_id>[0-9]+)$', views.customerdetail, name='customer_detail')
]
