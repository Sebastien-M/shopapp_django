# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import PricePlan


def index(request):
    template = loader.get_template('shop/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def new(request):
    pps = PricePlan.objects.all()
    # prices = pps.getget_price
    # product = PricePlan.products.though
    context = {'priceplans': pps}
    return render(request, 'shop/new.html', context)
