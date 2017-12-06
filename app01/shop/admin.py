# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contract, Custommer, Product, Period, PricePlan, Order


admin.site.site_header = 'App Test'

admin.site.register(Contract)
admin.site.register(Custommer)
admin.site.register(Product)
admin.site.register(Period)
admin.site.register(PricePlan)
admin.site.register(Order)
