# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import PricePlan, Order
from .forms import InfoForm
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'shop/index.html'


class PpView(generic.ListView):
    template_name = 'shop/new.html'
    context_object_name = 'priceplans'

    def get_queryset(self):
        return PricePlan.objects.all()


# def infos(request, priceplan_id):
#     priceplan = PricePlan.objects.get(pk=priceplan_id)
#     order = Order(priceplan=priceplan)
#     order.save()
#     form = InfoForm()
#     context = {'pp': priceplan, 'order': order, 'form': form}
#     return render(request, 'shop/infos.html', context)


class InfoView(generic.UpdateView):
    template_name = 'shop/infos.html'
    form_class = InfoForm
    # model = PricePlan
    success_url = '/shop'

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk', None)
        print(id)
        return PricePlan.objects.get(pk=id)

    def form_valid(self, form):
        return super(InfoView, self).form_valid(form)


def save(request, order_id):
    form = InfoForm(request.POST)
    order = Order.objects.get(pk=order_id)
    price_plan = PricePlan.objects.get(pk=order.priceplan.id)
    if form.is_valid():
        order.custommer_first_name = form.cleaned_data['first_name']
        order.custommer_last_name = form.cleaned_data['last_name']
        order.save()
        context = {'order': order}
        return render(request, 'shop/save.html', context)
    else:
        return render(request, 'shop/infos.html', {'pp': price_plan, 'order': order, 'form': form})


class OrderView(generic.ListView):
    template_name = 'shop/orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all()