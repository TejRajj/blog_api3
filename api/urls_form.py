from django.urls import path, include
from django.conf.urls import url
from . import views_form

urlpatterns = [
    path(r'form2/', views_form.index),

]
