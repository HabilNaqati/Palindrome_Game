from django.urls import path, include

urlpatterns = [
    path('api/', include('authentication.urls')),
    path('api/', include('user.urls')),
    path('api/', include('gamelogic.urls')),
]

handler404 = 'game.views.error_404_view'
