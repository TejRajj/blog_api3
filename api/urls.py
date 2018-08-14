from django.urls import path, include
from django.conf.urls import url
from . import views
from .views import login_list, login_detail, log
from .apiviews import (
    LoginList, LoginList_gen,
    LoginDetail, Create_more_gen,
    LoginDetail_more_gen,
    LoginList_more_gen,
    ProfileList
)




urlpatterns = [

#   LoginList_gen
    path('abc/', ProfileList, name='abc'),
    path("login/", LoginList.as_view(), name="login_list"),
    path("login_gen/", LoginList_gen.as_view(), name="login_gen"),
    path("login_gen_det/<int:pk>/", LoginDetail.as_view(), name="login_det"),
    path("login/<int:pk>/", LoginList.as_view(), name="login_detail"),

# More generic views
# ========================

    path("login_more_gen/", LoginList_more_gen.as_view(), name="login_more_gen"),
    path("loginDetail_more_gen/<int:pk>/", LoginDetail_more_gen.as_view(), name="loginDetail_more_gen"),
    path("create_more_gen/", Create_more_gen.as_view(), name="create_more_gen"),

# web-page
    url(r'^$', views.log)

]

