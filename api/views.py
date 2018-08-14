from django.shortcuts import render, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from .serializers import LoginSerializer
from .models import Login

# Create your views here.
def log(request):
    return render(request, 'account/login_page.html')

def login_list(request):
    login = Login.objects.all()
    data = {"detail": list(login.values("Full_name", "Country"))}
    return JsonResponse(data)   

def login_detail(request, pk):
    login = get_object_or_404(Login, pk=pk)
    data = {"results": {
        "question": login.question,
        "created_by": login.created_by.username,
        "pub_date": login.pub_date
    }}
    return JsonResponse(data)

def log(request):
    numbers = [1,2,3]
    name = "Tejas Manakr"
    arg = {'a' : numbers, 'name':name}
    return render(request, 'account/login_page.html', arg)