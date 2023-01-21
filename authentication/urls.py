from django.urls import path
from authentication.views import AuthenticationViewSet
# ===========================================================
# @End Points
# ===========================================================
urlpatterns = [
    path('login/', AuthenticationViewSet.as_view()),
]
