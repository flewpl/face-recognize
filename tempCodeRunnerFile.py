img = cv2.imread('images/images.jpg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces= cv2.CascadeClassifier('faces.xml')

results = faces.detectMultiScale(grey, scaleFactor =1.1, minNeighbors =3 )

for(x,y,w,h) in results:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), thickness=2)



cv2.imshow('Result',img)
cv2.waitKey(0)