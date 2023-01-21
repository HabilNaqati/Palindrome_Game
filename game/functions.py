import jwt
from rest_framework import status
from rest_framework.response import Response
from user.models import User
from user.serializers import UserSerializer
# ===========================================================
# @Methods
# ===========================================================


'''------------------------------------
             verifyJWT
------------------------------------'''


def verifyJWT(request):
    try:
        if 'Authorization' in request.headers:
            authHeaders = str(request.headers['authorization'])
            token = authHeaders.strip('Bearer').lstrip()
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            if not payload['id']:
                raise Exception

            user_object = User.objects.get(pk=payload['id'])
            result = UserSerializer(user_object)
            if not result:
                raise Exception

            return Response(result.data,
                            status=status.HTTP_200_OK)
        else:
            return Response({'message': "Bearer Token Missing!"},
                            status=status.HTTP_403_FORBIDDEN)
    except Exception as e:
        return Response({'message': "Invalid Token!"},
                        status=status.HTTP_403_FORBIDDEN)


'''------------------------------------
             getUserId
------------------------------------'''


def getUserId(request):
    response = verifyJWT(request)
    if (response.status_code == 200):
        return {"userId": response.data['userId']}
    else:
        return response
