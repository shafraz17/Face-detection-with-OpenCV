# Face-detection-with-OpenCV

First clone the repo to your pc

What is this haarcascade xml files??
    They are stored with information of the eyes and face.
    
As the first step install OpenCV library using the follwing command
    pip3 install opencv-python
    
Finally run the python file

Explanation :-

```
import cv2
import numpy as np
```
This imports the packages required for the face detection

```
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
```
Import the haarcacade files that has the features in XML format

```
cap = cv2.VideoCapture(0)
```
This function is called to turn on the camera '0' is used for primary cam. (Web cam)

```
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
Reads the input from the camera, and converted the image into a grayscale image

```
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
```
Detects the cordinates of the face in the image according to the features described in the haarcascade files

```
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
```
This forms a rectangular around the detected face using the x,y,w,h cordinates.
x,y refers to the left top corner cordinate and w,h is width and height respectively

```
face_gray = gray[y:y+h, x:x+w]
face_color = img[y:y+h, x:x+w]
```
According to the cordinates, height and width the face is croped from the grayscale image and stored in face_gray
face_color sotres the croped image with the original colors.

```
cv2.rectangle(img, ((0,img.shape[0] -25)),(270, img.shape[0]), (255,255,255), -1)
cv2.putText(img, "Number of views detected: " + str(faces.shape[0]), (0,img.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
```
This creates a rectangular to dispaly the number of detected faces on the camera. This is displayed at the bottom left corner of the camera window.

```
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
```
Similar to the face detection this part detects the eyes within the faces detected

```
cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 113:
        break
```
It shows the detected faces. Now it waits to end the process. So you have to press Q to quit the camera.

```
cap.release()
cv2.destroyAllWindows()
```
Thme camera is release and all windows are destroyed.



    
