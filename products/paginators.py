from rest_framework.pagination import PageNumberPagination


class CustomPaginator(PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    max_page_size = 100
