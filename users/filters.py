import django_filters
from users.models import User

class UserFilters(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter')

    class Meta:
        model = User
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(name__icontains=value)