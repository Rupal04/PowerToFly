from rest_framework.pagination import PageNumberPagination

from powertofly.settings import DEFAULT_PAGE_SIZE


"""
The Custom Pagination class that is used for showing the pagination implementation 
"""


class CustomPageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = 100

    @property
    def num_pages(self):
        return self.page.paginator.num_pages

    @property
    def pagination_data(self):
        return {
            'page_count': self.num_pages,
            'total_entries': self.page.paginator.count,
            'next_page_link': self.get_next_link(),
            'previous_page_link': self.get_previous_link(),
        }