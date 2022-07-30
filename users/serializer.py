from rest_framework import serializers as sz
from users.models import User

"""
User Serializer that is need for serializing the user data
"""


class UserSerializer(sz.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'