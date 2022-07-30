import json
import redis

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from powertofly.pagination import CustomPageNumberPagination
from users.filters import UserFilters
from users.keys import get_user_list, CacheNameSpace
from users.models import User
from users.serializer import UserSerializer

r_cache = redis.StrictRedis()


class UserView(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilters

    def get_queryset(self):
        return User.objects.all()

    def list(self, request, *args, **kwargs):
        page_number = self.request.query_params.get('page', 1)

        """
        This if/else section of the code is written to show the caching mechanism in the 
        most simplest way. 
        Here we have cached only the data of page number 1 and if the page number is something
        other than 1, we are not maintaining the caching and its working casually. 
        """
        if page_number == 1:
            if 'user_list' in r_cache:
                # Getting the data from the cache
                response = json.loads(r_cache.get('user_list'))
            else:
                list_response = super().list(request, *args, **kwargs)
                response = {
                    'data': list_response.data['results'],
                    'pagination_meta': self.paginator.pagination_data,
                }
                # setting the cache
                r_cache.set(get_user_list(), json.dumps(response),
                            CacheNameSpace.USER_LIST_PAGE_1[1])

        else:
            list_response = super().list(request, *args, **kwargs)
            response = {
                'data': list_response.data['results'],
                'pagination_meta': self.paginator.pagination_data,
            }

        return Response(response, status=status.HTTP_200_OK)