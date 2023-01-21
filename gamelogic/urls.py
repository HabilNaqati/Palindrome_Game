from django.urls import path
from .views import GameAPI
# ===========================================================
# @End Points
# ===========================================================
urlpatterns = [
    path('game/', GameAPI.as_view()),
    path('game/<int:pk>', GameAPI.as_view()),
]
