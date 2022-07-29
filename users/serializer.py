from rest_framework import serializers as sz
from users.models import User


class UserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'