from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 7
    page_size_query = 'size'
    page_query_param = 'p'
    max_page_size = 10
    last_page_strings = 'end'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'