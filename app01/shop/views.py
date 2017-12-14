# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import PricePlan, Order
from .forms import InfoForm
from django.views import generic
import stomp
import json
from .services import CustomerService


class IndexView(generic.TemplateView):
    template_name = 'shop/index.html'


class PpView(generic.ListView):
    template_name = 'shop/new.html'
    context_object_name = 'priceplans'

    def get_queryset(self):
        return PricePlan.objects.all()


def info(request, priceplan_id):
    priceplan = PricePlan.objects.get(pk=priceplan_id)
    form = InfoForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        order = Order(priceplan=priceplan,
                      custommer_first_name=form.cleaned_data['first_name'],
                      custommer_last_name=form.cleaned_data['last_name'])
        order.save()
        tosend = dict()
        tosend['priceplan_id'] = order.priceplan.id
        tosend['priceplan_code'] = order.priceplan.code
        tosend['priceplan_price'] = order.priceplan.get_price
        tosend['first_name'] = order.custommer_first_name
        tosend['last-name'] = order.custommer_last_name
        tosend['age'] = form.cleaned_data['age']
        tosend['number'] = form.cleaned_data['number']
        tosend = json.dumps(tosend, ensure_ascii=False)
        send_to_queue(tosend)
        context = {'order': order}
        return render(request, 'shop/save.html', context)

    context = {'pp': priceplan, 'form': form}
    return render(request, 'shop/infos.html', context)


# class InfoView(generic.UpdateView):
#     template_name = 'shop/infos.html'
#     form_class = InfoForm
#     # model = PricePlan
#     success_url = '/shop'
#
#     def get_object(self, queryset=None):
#         id = self.kwargs.get('pk', None)
#         print(id)
#         return PricePlan.objects.get(pk=id)
#
#     def form_valid(self, form):
#         return super(InfoView, self).form_valid(form)


def save(request, order_id):
    form = InfoForm(request.POST)
    order = Order.objects.get(pk=order_id)
    price_plan = PricePlan.objects.get(pk=order.priceplan.id)
    if form.is_valid():
        order.custommer_first_name = form.cleaned_data['first_name']
        order.custommer_last_name = form.cleaned_data['last_name']
        order.save()
        send_to_queue(order)
        context = {'order': order}
        return render(request, 'shop/save.html', context)
    else:
        return render(request, 'shop/infos.html', {'pp': price_plan, 'order': order, 'form': form})


class OrderView(generic.ListView):
    template_name = 'shop/orders.html'
    context_object_name = 'customers'

    def get_queryset(self):
        service = CustomerService()
        customers = service.getallcustomers()
        print customers
        # json.loads(customers)

        print(customers[0]['first_name'])
        return customers


def send_to_queue(element):
    conn = stomp.Connection()
    conn.start()
    conn.connect()
    conn.send(body=str(element), destination='/queue/orders')
    conn.disconnect()


def productlisting(priceplan):
    products = []
    for product in priceplan:
        products.append([product.code, product.price, product.description])
    return products
