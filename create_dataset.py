import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 1280) 
cam.set(4, 720) 

face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

face_id = input('\nEnter an ID for your face: ')

print("\n1..2..3..Look at the camera ")
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+(w+30),y+(h+30)), (255,0,0), 2)     
        count += 1

        cv2.imwrite("dataset/person." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff 
    if k == 27:
         break
    elif count >= 40: 
         break

cam.release()
cv2.destroyAllWindows()


