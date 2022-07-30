import django_filters
from django.db.models import Q
from users.models import User


"""
Filter class that shows the working of filter mechanism based on name (firstname/lastnames)
"""


class UserFilters(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = User
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(Q(first_name__icontains=value) | Q(last_name__icontains=value))