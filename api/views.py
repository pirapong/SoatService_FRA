from rest_framework.response import Response
from rest_framework.decorators import api_view
from faceRecognition.views import fra
from .views import *
import base64
from PIL import Image
from io import BytesIO

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
    img_resize = resize_image_base64(request.data['base64'],1000,1280)
    base64_string = img_resize
    key = request.data['key']
    image = base64.b64decode(base64_string, validate=True)
    file_to_save = "imgDb/" + key + ".jpg"
    with open(file_to_save, "wb") as f:
        f.write(image)
    
    return Response('ok')


def resize_image_base64(base64_str, new_width, new_height):
    # Decode the base64 string
    image_data = base64.b64decode(base64_str)
    image = Image.open(BytesIO(image_data))

    # Resize the image
    resized_image = image.resize((new_width, new_height))
    
    # Encode the resized image back to base64
    buffered = BytesIO()
    resized_image.save(buffered, format="PNG")
    resized_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    print(resized_base64)    
    return resized_base64

    # # Example usage
    # original_base64 = "your_base64_string_here"
    # resized_base64 = resize_image_base64(original_base64, new_width=100, new_height=100)
    # print(resized_base64)