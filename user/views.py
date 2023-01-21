from rest_framework import status
from rest_framework.views import APIView
from user.serializers import UserSerializer
from user.models import User
from game.functions import getUserId
from django.http import JsonResponse
from datetime import date


class UserViewSet(APIView):

    # GET USER
    def get(self, request):
        try:
            response = getUserId(request)
            if 'userId' in response:
                if response['userId']:
                    user = User.objects.get(pk=response['userId'])
                    result = UserSerializer(user)
                else:
                    JsonResponse({"output": "Unauthorized"},
                                 status=status.HTTP_403_FORBIDDEN)
                return JsonResponse({"output": result.data}, status=status.HTTP_200_OK)
            else:
                return response
        except:
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)

    # CREATE USER
    def post(self, request, format=None):
        try:
            user = request.data
            result = UserSerializer(data=user)
            if result.is_valid():
                result.save()
                return JsonResponse({"output": result.data}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"message": "Invalid Data", "Error": result.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)

    # UPDATE USER
    def put(self, request):
        try:
            response = getUserId(request)
            if 'userId' in response:
                try:
                    if response['userId']:
                        user = User.objects.get(pk=response['userId'])
                    else:
                        JsonResponse({"output": "Unauthorized"},
                                     status=status.HTTP_403_FORBIDDEN)
                except:
                    return JsonResponse({"message": "No User Found!!!"}, status=status.HTTP_404_NOT_FOUND)
                request.data['userEntryId'] = response['userId']
                request.data['userModifiedId'] = response['userId']
                request.data['userModifiedDate'] = date.today().isoformat()
                result = UserSerializer(
                    instance=user, data=request.data, partial=True)
                if result.is_valid():
                    result.save()
                    return JsonResponse({"output": result.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"message": "Invalid Data", "Error": result.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response
        except:
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)

    # DELETE USER
    def delete(self, request):
        try:
            response = getUserId(request)
            if 'userId' in response:
                try:
                    if response['userId']:
                        user = User.objects.get(pk=response['userId'])
                    else:
                        JsonResponse({"output": "Unauthorized"},
                                     status=status.HTTP_403_FORBIDDEN)
                except:
                    return JsonResponse({"message": "No User Found!!!"}, status=status.HTTP_404_NOT_FOUND)
                user.delete()
                return JsonResponse({"message": "User Deleted Successfully"}, status=status.HTTP_200_OK)
            else:
                return response
        except:
            return JsonResponse({"message": "Bad Request!!!"}, status=status.HTTP_404_NOT_FOUND)
