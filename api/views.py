from rest_framework.response import Response
from rest_framework.decorators import api_view
from faceRecognition.views import fra
from .views import *
import base64
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
    
    
@api_view(['POST'])
def uploadDb(request):
    base64_string = request.data['base64']
    key = request.data['key']
    image = base64.b64decode(base64_string, validate=True)
    file_to_save = "imgDb/" + key + ".jpg"
    with open(file_to_save, "wb") as f:
        f.write(image)
    return Response('ok')