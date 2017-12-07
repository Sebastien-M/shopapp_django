# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Contract, Custommer, Product, Period, PricePlan, Order
from django import forms


admin.site.site_header = 'App Test'


class ProductForm(forms.ModelForm):
    model = Product

    def clean(self):
        code = self.cleaned_data.get('code')
        if len(code) > 20:
            raise forms.ValidationError('Code must contains 20 characters or less')
        return self.cleaned_data


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm


admin.site.register(Contract)
admin.site.register(Custommer)
admin.site.register(Product, ProductAdmin)
admin.site.register(Period)
admin.site.register(PricePlan)
admin.site.register(Order)
