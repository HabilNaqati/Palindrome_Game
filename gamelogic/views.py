from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import GameSerializer
from .models import Game
from game.pagination import CustomPagination
import random
import string
from string import digits
from game.functions import getUserId
from datetime import date

# ===========================================================
# @Controller or @Views
# ===========================================================

'''----------@Post Start Game----------'''


class GameAPI(APIView):

    pagination_class = CustomPagination
    '''----------@Post Start Game----------'''

    def post(self, request, format=None):
        try:
            response = getUserId(request)
            if 'userId' in response:
                game = {}
                game['gameName'] = ""
                game['gameEntryId'] = response['userId']
                result = GameSerializer(data=game)
                if result.is_valid():
                    result.save()
                    return JsonResponse({"output": result.data}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({"message": "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)

    '''----------@Put Update Game----------'''

    def put(self, request, pk=None, format=None):
        remove_digits = str.maketrans('', '', digits)
        try:
            response = getUserId(request)
            if 'userId' in response:
                try:
                    game = Game.objects.get(pk=pk)
                    game.gameModifiedId = response['userId']
                    game.gameModifiedDate = date.today().isoformat()
                    if len(game.gameName) >= 6:
                        game.gameName = ""
                        game.save()
                        return JsonResponse({"status": "Game Restarted. Start Again!"})

                    char = request.data['char']
                    if char not in string.ascii_lowercase:
                        return JsonResponse({"error": "Invalid character"})

                    game.gameName += char
                    game.gameName += str(random.randint(0, 9))
                    game.save()

                    if len(game.gameName) == 6:
                        if game.gameName.translate(remove_digits) == game.gameName[::-1].translate(remove_digits):
                            return JsonResponse({"status": "Palindrome"}, status=status.HTTP_200_OK)
                        else:
                            return JsonResponse({"status": "Not Palindrome"}, status=status.HTTP_200_OK)
                    else:
                        return JsonResponse({"status": "Continue"}, status=status.HTTP_200_OK)
                except Game.DoesNotExist:
                    return JsonResponse({"error": "Invalid game ID"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response
        except Exception as e:
            print(e)
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)
    '''----------@Get Partticular Game by ID or All Games----------'''

    def get(self, request, pk=None, format=None):
        try:
            response = getUserId(request)
            if 'userId' in response:
                try:
                    paginator = CustomPagination()
                    if pk:
                        game = Game.objects.get(pk=pk)
                        result = GameSerializer(game)
                    else:
                        querySet = Game.objects.all()
                        paginationOutput = CustomPagination.getPagination(paginator,
                                                                          querySet, request)
                        result = GameSerializer(
                            paginationOutput, many=True)
                        return JsonResponse({"result": paginator.get_paginated_response(result.data)}, status=status.HTTP_200_OK)

                except:
                    return JsonResponse({"message": "Invalid game ID!"}, status=status.HTTP_404_NOT_FOUND)
                return JsonResponse({"output": result.data}, status=status.HTTP_200_OK)
            else:
                return response
        except:
            return JsonResponse({"message": "Bad request!!!"}, status=status.HTTP_400_BAD_REQUEST)
