# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import generic


def index(request):
    return HttpResponse("Shop index")

