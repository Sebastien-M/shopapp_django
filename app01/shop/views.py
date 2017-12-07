# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import PricePlan, Order
from .forms import InfoForm


def index(request):
    template = loader.get_template('shop/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def new(request):
    pps = PricePlan.objects.all()
    context = {'priceplans': pps}
    return render(request, 'shop/new.html', context)


def infos(request, priceplan_id):
    priceplan = PricePlan.objects.get(pk=priceplan_id)
    order = Order(priceplan=priceplan)
    order.save()
    form = InfoForm()
    context = {'pp': priceplan, 'order': order, 'form': form}
    return render(request, 'shop/infos.html', context)


def save(request, order_id):
    form = InfoForm(request.POST)
    order = Order.objects.get(pk=order_id)
    price_plan = PricePlan.objects.get(pk=order.priceplan.id)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']

        order.custommer_first_name = first_name
        order.custommer_last_name = last_name
        order.save()
        context = {'order': order}
        return render(request, 'shop/save.html', context)
    else:
        return render(request, 'shop/infos.html', { 'pp': price_plan, 'order': order, 'form': form})


def orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request,'shop/orders.html', context)
