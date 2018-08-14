from .models import Login
from rest_framework.response import Response
from django.shortcuts import render, redirect
import requests


def form(request):
    return render(request, 'account/login_page.html')
# http://127.0.0.1:8000/login/?format=json


def index(request):
    url = 'http://127.0.0.1:8000/login_page/login_gen_det/'
    id = '1'
    url_id = url+id

    db = Login.objects.all()

    db2 = []

    for id in db:
        r = requests.get(url_id.format(id)).json()

        login_detail = {
            'id': id.id,
            'Full_name': r['Full_name'],
            'Country': r['Country'],
        }

        db2.append(login_detail)
    print(db2)
    context = {'db2': db2}
    return render(request, 'account/login_page.html', context)