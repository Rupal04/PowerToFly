from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from powertofly.pagination import CustomPageNumberPagination
from users.filters import UserFilters
from users.models import User
from users.serializer import UserSerializer


class UserView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilters

    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        list_response = super().list(request, *args, **kwargs)
        response = {
            'data': list_response.data['results'],
            'pagination_meta': self.paginator.pagination_data,
        }
        return Response(response, status=status.HTTP_200_OK)