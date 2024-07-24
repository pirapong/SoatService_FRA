from django.shortcuts import  HttpResponse
from .models import *
import face_recognition
from django.db.models import Q
import base64, binascii

def fra(request):
    # base64_string = open('data.txt', 'r').read()
    base64_string = request.data['base64']
    key = request.data['key']
    image = base64.b64decode(base64_string, validate=True)
    file_to_save = "img/" + key + ".jpg"
    #with open(file_to_save, "wb") as f:
    #    f.write(image)
    imgDb = face_recognition.load_image_file('imgDb/img.jpg')
    imgDb_encoding = face_recognition.face_encodings(imgDb)[0]
    imgDv = face_recognition.load_image_file(file_to_save)
    imgDv_encoding = face_recognition.face_encodings(imgDv)[0]

    for x in range(1, 100):
        results = face_recognition.compare_faces([imgDv_encoding], imgDb_encoding,x/100)
        if results[0] == True:
            print("เปอร์เซนต์ความถูกต้อง %d" % ((x-100) * (-1)))
            avg = "Accuracy %d " % ((x-100) * (-1)) + "%"
            break

    return avg
