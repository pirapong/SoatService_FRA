from django.shortcuts import  HttpResponse
from .models import *
import face_recognition
import base64

def fra(request):
##    #base64_string = open('data.txt', 'r').read()
    base64_string = request.data['base64']
    key = request.data['key']
    image = base64.b64decode(base64_string)
#
    file_to_save = "/home/test/SoatService_FRA/media/img/" + str(key) + ".jpg"
    file_to_check = "/home/test/SoatService_FRA/media/imgDb/" + str(key) + ".jpg"
    with open(file_to_save, "wb") as f:
        f.write(image)
        
    print(file_to_check)
    imgDb = face_recognition.load_image_file(file_to_check)
    imgDb_encoding = face_recognition.face_encodings(imgDb,model='large',num_jitters=10)[0]
    imgDv = face_recognition.load_image_file(file_to_save)
    imgDv_encoding = face_recognition.face_encodings(imgDv,model='large',num_jitters=10)[0]

    for x in range(1, 100):
        results = face_recognition.compare_faces([imgDv_encoding], imgDb_encoding,x/100)
        if results[0] == True:
            print("เปอร์เซนต์ความถูกต้อง %d" % ((x-100)  * (-1)))
            print("เปอร์เซนต์ความถูกต้อง %d" % ((((x-100)*100) / 80)  * (-1)))
            avg1 = "Accuracy %d " % ((((x-100)*100) / 80)  * (-1)) + "%"
            avg = "Accuracy %d " % ((x-100)  * (-1)) + "%"
            break

    return avg
