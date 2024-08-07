from rest_framework.response import Response
from rest_framework.decorators import api_view
from faceRecognition.views import fra
from .views import *
import base64
from PIL import Image
# from io import BytesIO
# import math
import cv2


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

    #img_resize = resize_image_base64(request.data['base64'],1280,1000)
    base64_string = request.data['base64']
    key = request.data['key']
    image = base64.b64decode(base64_string, validate=True)
    file_to_save = "/home/test/SoatService_FRA/media/imgDb/" + key + ".jpg"
    with open(file_to_save, "wb") as f:
        f.write(image)
    
    im = cv2.imread(file_to_save)
    h, w, c = im.shape
    
    if h >= 1509 and w >= 1084:
        resize_image(file_to_save, file_to_save, (1084,1509))
    
    return Response('ok')



def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        resized_img = img.resize(size, Image.LANCZOS)
        rotated_img = img.rotate(270, expand=True, resample=Image.LANCZOS)
        rotated_img.save(output_path)

