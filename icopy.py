import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(1)
count=0


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    
    #print("Total number of Faces found",len(faces))

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        face_gray = gray[y:y+h, x:x+w]
        face_color = img[y:y+h, x:x+w]

        cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
        cv2.putText(img, "Number of views detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
        

        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    # if (len(faces) == 1):
    #     print("1 face found")
    # else:
    #     print(format(len(faces)), " faces found")

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 113:
        break

cap.release()
cv2.destroyAllWindows()


