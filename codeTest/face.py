# import face_recognition
# import numpy as np 
# import cv2




# # rotated_image = rotate_image(img, 197)

# # imgDb = face_recognition.load_image_file('imgDb/22.jpg')
# # imgDb_encoding = face_recognition.face_encodings(imgDb,model='large',num_jitters=100)[0]
# # imgDv = face_recognition.load_image_file('img/11.jpg')
# # imgDv_encoding = face_recognition.face_encodings(imgDv,model='large',num_jitters=100)[0]

# # face_locations = face_recognition.face_locations(imgDb, model="cnn")
# # face_encodings = face_recognition.face_encodings(imgDb, face_locations)[0]


# # face_locations1 = face_recognition.face_locations(imgDv, model="cnn")
# # face_encodings1 = face_recognition.face_encodings(imgDv, face_locations1)[0]

# # known_face_encodings = [face_encodings]

# # for sss in face_encodings1:
# #     face_distances = face_recognition.face_distance(known_face_encodings, face_encodings1)

# #     best = np.argmin(face_distances)
# #     face_percent_value = 1-face_distances[best]
# #     print(face_percent_value)


# # for x in range(1, 100):
# #     results = face_recognition.compare_faces([imgDv_encoding], imgDb_encoding,x/100)
# #     if results[0] == True:
# #         print("เปอร์เซนต์ความถูกต้อง %d" % ((x-100)  * (-1)))
# #         # print("เปอร์เซนต์ความถูกต้อง %d" % ((((x-100)*100) / 80)  * (-1)))
# #         # avg = "Accuracy %d " % ((((x-100)*100) / 80)  * (-1)) + "%"
# #         break




# # def rotate_image(arr, angle):
# img = cv2.imread('imgDb/ba13.jpg',1)
# arr = 270
# height, width = arr.shape[:2]
# image_center = (width/2, height/2)
# rotation_arr = cv2.getRotationMatrix2D(image_center, angle, 1)
# abs_cos = abs(rotation_arr[0,0])
# abs_sin = abs(rotation_arr[0,1])
# bound_w = int(height * abs_sin + width * abs_cos)
# bound_h = int(height * abs_cos + width * abs_sin)
# rotation_arr[0, 2] += bound_w/2 - image_center[0]
# rotation_arr[1, 2] += bound_h/2 - image_center[1]
# rotated_mat = cv2.warpAffine(arr, rotation_arr, (bound_w, bound_h))
# # return rotated_mat

# # import face_recognition as face 
# # import numpy as np 
# # import cv2

# # #ORIGINAL_CODE_CREDIT:  https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_webcam_faster.py

# # #ดึงวิดีโอตัวอย่างเข้ามา, ถ้าต้องการใช้webcamให้ใส่เป็น0
# # video_capture = cv2.VideoCapture("sample.mp4") 

# # #ใบหน้าคนที่ต้องการรู้จำเป็นreference #คนที่1
# # pop_image = face.load_image_file("pop.jpg")
# # pop_face_encoding = face.face_encodings(pop_image)[0]

# # #ใบหน้าคนที่ต้องการรู้จำเป็นreference #คนที่2
# # oat_image = face.load_image_file("oat.jpg")
# # oat_face_encoding = face.face_encodings(oat_image)[0]

# # #ประกาศตัวแปร
# # face_locations = []
# # face_encodings = []
# # face_names = []
# # face_percent = []
# # #ตัวแปรนี้ใช้สำหรับคิดเฟรมเว้นเฟรมเพื่อเพิ่มfps 
# # process_this_frame = True

# # known_face_encodings = [pop_face_encoding, oat_face_encoding]
# # known_face_names = ["PONGKUL", "PRAMOTE"]

# # #loopคำนวณแต่ละเฟรมของวิดีโอ
# # while True:
# #     #อ่านค่าแต่ละเฟรมจากวิดีโอ
# #     ret, frame = video_capture.read()
# #     if ret:
# #         #ลดขนาดสองเท่าเพื่อเพิ่มfps 
# #         small_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
# #         #เปลี่ยน bgrเป็น rgb 
# #         rgb_small_frame = small_frame[:,:,::-1]

# #         face_names = []
# #         face_percent = []

# #         if process_this_frame:
# #             #ค้นหาตำแหน่งใบหน้าในเฟรม 
# #             face_locations = face.face_locations(rgb_small_frame, model="cnn")
# #             #นำใบหน้ามาหาfeaturesต่างๆที่เป็นเอกลักษณ์ 
# #             face_encodings = face.face_encodings(rgb_small_frame, face_locations)
            
# #             #เทียบแต่ละใบหน้า
# #             for face_encoding in face_encodings:
# #                 face_distances = face.face_distance(known_face_encodings, face_encoding)
# #                 best = np.argmin(face_distances)
# #                 face_percent_value = 1-face_distances[best]

# #                 #กรองใบหน้าที่ความมั่นใจ50% ปล.สามารถลองเปลี่ยนได้
# #                 if face_percent_value >= 0.5:
# #                     name = known_face_names[best]
# #                     percent = round(face_percent_value*100,2)
# #                     face_percent.append(percent)
# #                 else:
# #                     name = "UNKNOWN"
# #                     face_percent.append(0)
# #                 face_names.append(name)

# #         #วาดกล่องและtextเมื่อแสดงผลออกมาออกมา
# #         for (top,right,bottom, left), name, percent in zip(face_locations, face_names, face_percent):
# #             top*= 2
# #             right*= 2
# #             bottom*= 2
# #             left*= 2

# #             if name == "UNKNOWN":
# #                 color = [46,2,209]
# #             else:
# #                 color = [255,102,51]

# #             cv2.rectangle(frame, (left,top), (right,bottom), color, 2)
# #             cv2.rectangle(frame, (left-1, top -30), (right+1,top), color, cv2.FILLED)
# #             cv2.rectangle(frame, (left-1, bottom), (right+1,bottom+30), color, cv2.FILLED)
# #             font = cv2.FONT_HERSHEY_DUPLEX
# #             cv2.putText(frame, name, (left+6, top-6), font, 0.6, (255,255,255), 1)
# #             cv2.putText(frame, "MATCH: "+str(percent)+"%", (left+6, bottom+23), font, 0.6, (255,255,255), 1)


# #         #สลับค่าเป็นค่าตรงข้ามเพื่อให้คิดเฟรมเว้นเฟรม
# #         process_this_frame = not process_this_frame

# #         #แสดงผลลัพท์ออกมา
# #         cv2.imshow("Video", frame)
# #         if cv2.waitKey(1) & 0xFF == ord('q'):
# #             break

# #     else:
# #         break

# # #ล้างค่าต่างๆเมื่อปิดโปรแกรม
# # video_capture.release()
# # cv2.destroyAllWindows()




import cv2
import math

def rotate_image(array, angle):
   height, width = array.shape[:2]
   image_center = (width / 2, height / 2)
   
   rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1)
   
   radians = math.radians(angle)
   sin = math.sin(radians)
   cos = math.cos(radians)
   bound_w = int((height * abs(sin)) + (width * abs(cos)))
   bound_h = int((height * abs(cos)) + (width * abs(sin)))
   
   rotation_mat[0, 2] += ((bound_w / 2) - image_center[0])
   rotation_mat[1, 2] += ((bound_h / 2) - image_center[1])
   
   rotated_mat = cv2.warpAffine(array, rotation_mat, (bound_w, bound_h))
   return rotated_mat

img = cv2.imread('imgDb/ba11.jpg',1)
rotated_image = rotate_image(img, 90)

cv2.imshow('Rotated image', rotated_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()