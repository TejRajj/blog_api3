from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Login
from .serializers import LoginSerializer
from rest_framework import generics
from django.shortcuts import render, redirect
from rest_framework.renderers import TemplateHTMLRenderer

class ProfileList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request, pk):
        profile = get_object_or_404(Login, pk=pk)
        serializer = LoginSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(Login, pk=pk)
        serializer = LoginSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('profile-list')





def abc(request):
    login = Login.objects.all()
    print(request.POST)
    context = {'aa':login}
    return render(request,"account/home.html",context)



















class LoginList(APIView):
    def get(self, request):
        login = Login.objects.all()
        data = LoginSerializer(login, many= True).data
        return Response(data)

class LoginList_gen(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

class LoginDetail(generics.RetrieveDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer

#   More generic views
#   ============================
class LoginList_more_gen(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer


class LoginDetail_more_gen(generics.RetrieveDestroyAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer


class Create_more_gen(generics.CreateAPIView):
    serializer_class = LoginSerializer