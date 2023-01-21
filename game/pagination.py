from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    def getPagination(paginator, query, req):
        result_page = paginator.paginate_queryset(
            query, req)
        return result_page

    def get_paginated_response(self, data):
        return ({
            'pagination': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            # 'page_size': 10,
            'output': data
        })
