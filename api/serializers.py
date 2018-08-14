from rest_framework import serializers
from .models import Login

#to built API
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Login
        fields = '__all__'


class LoginSerializer2(serializers.Serializer):
    email = serializers.EmailField(
        max_length=100,
        style={'placeholder': 'Email', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    remember_me = serializers.BooleanField()
