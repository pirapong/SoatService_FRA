from rest_framework.response import Response
from rest_framework.decorators import api_view
from faceRecognition.views import fra
from .views import *
# from .serializers import ItemSerializer
# import face_recognition   


# @api_view(['POST'])
# def getFace(request):
#     # # fa()
#     # serializer = ItemSerializer(data=request.data)
#     # if serializer.is_valid():
#     #     serializer.save()
#     print('adfasdf')
#     return Response(request)

@api_view(['POST'])
def getFace(request):
    results = fra(request)
    return Response(results)
    