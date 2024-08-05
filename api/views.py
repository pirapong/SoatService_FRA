from rest_framework.response import Response
from rest_framework.decorators import api_view
from faceRecognition.views import fra
from .views import *
import base64
# from PIL import Image
# from io import BytesIO
# import math
# import cv2


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
    file_to_save = "/home/test/SoatService_FRA/media/imgs/" + key + ".jpg"
    with open(file_to_save, "wb") as f:
        f.write(image)
    
    return Response('ok')




# def resize_image_base64(base64_str, new_width, new_height):
#     # Decode the base64 string
#     image_data = base64.b64decode(base64_str)
#     image = Image.open(BytesIO(image_data))

#     # Resize the image
#     resized_image = image.resize((new_width, new_height))
    
#     # Encode the resized image back to base64
#     buffered = BytesIO()
#     #resized_image.save(buffered, format="PNG")
#     resized_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
#     print(resized_base64)    
#     return resized_base64

    # # Example usage
    # original_base64 = "your_base64_string_here"
    # resized_base64 = resize_image_base64(original_base64, new_width=100, new_height=100)
    # print(resized_base64)


# def rotate_image(array, angle):
#     height, width = array.shape[:2]
#     image_center = (width / 2, height / 2)
   
#     rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)
   
#     radians = math.radians(angle)
#     sin = math.sin(radians)
#     cos = math.cos(radians)
#     bound_w = int((height * abs(sin)) + (width * abs(cos)))
#     bound_h = int((height * abs(cos)) + (width * abs(sin)))
   
#     rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
#     rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])
   
#     rotated_mat = cv2.warpAffine(array, rotation_mat, (bound_w, bound_h))
#     return rotated_mat

# img = cv2.imread('imgDb/ba11.jpg',1)
# rotated_image = rotate_image(img, 90)
