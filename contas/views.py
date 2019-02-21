from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    #html = "<html><body>It is now {}.</body></html>".format(now)
    return render(request, 'contas/home.html', data)