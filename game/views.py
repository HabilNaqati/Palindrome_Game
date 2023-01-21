from django.http import JsonResponse
from rest_framework import status


def error_404_view(request, exception):
    return JsonResponse({"message": "Invalid url"}, status=status.HTTP_404_NOT_FOUND)
