import cv2
import numpy as np
# photo = np.zeros((500,500,3), dtype='uint8')
# # photo[:] = 0,255,0
# photo = cv2.rectangle(photo, (150,150), (350,350),(0,255,255), thickness=2)
# # photo= cv2.circle(photo, (photo.shape[1]//2,(photo.shape[0]//2)),50, (0,255,0), thickness=1)
# # photo = cv2.line(photo, (150,150),(350,350),(128, 0, 128), thickness=2 )
# # photo = cv2.line(photo, (150,350),(350,150),(128, 0, 128), thickness=2 )
# photo = cv2.putText(photo, 'Me',(photo.shape[1]//2 - 25,photo.shape[0]//2),cv2.FONT_HERSHEY_TRIPLEX,1,(0,255,255),thickness=2)

# cv2.imshow('Photo', photo)
# cv2.waitKey(0)

cap = cv2.VideoCapture("film/video.mp4")
cap.set(3, 500)
cap.set(4, 300)

while True:
    success, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break