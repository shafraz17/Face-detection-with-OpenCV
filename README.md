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





    
