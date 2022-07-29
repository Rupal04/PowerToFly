from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from users.models import User
from users.serializer import UserSerializer


class UserView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()