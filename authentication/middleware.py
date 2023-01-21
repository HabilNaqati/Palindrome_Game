import datetime
import jwt
from rest_framework.response import Response

# ===========================================================
# @Methods
# ===========================================================


class JWT:
    def getJWT(user):
        payload = {
            'id': user.userId,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow(),
            'userRoleId': user.userRoleId,
            'userActive': user.userActive
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'token': token
        }

        return response
