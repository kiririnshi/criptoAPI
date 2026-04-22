from datetime import datetime, timezone
from decimal import Decimal
import json
import requests

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from coins.models import Precio

def show_graph(request):
    if(request.method == 'GET'):
        template = loader.get_template('index.html')
        return HttpResponse(template.render())
