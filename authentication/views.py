from rest_framework import status
from rest_framework.views import APIView
from user.models import User
from user.serializers import UserSerializer
from authentication.middleware import JWT
from game.functions import getUserId
from django.http import JsonResponse

# ===========================================================
# @Controller or @Views
# ===========================================================


class AuthenticationViewSet(APIView):

    '''@Post Generate Jwt Token'''

    def post(self, request):
        userName = request.data['username']
        userPassword = request.data['password']
        user = User.objects.filter(
            userEmail=userName, userUpass=userPassword).first()
        if user is None:
            return JsonResponse({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        response = JWT.getJWT(user)
        return response
