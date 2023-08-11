import cv2
face_cascade = cv2.CascadeClassifier(r'E:\cv lab\haarcascade_frontalface_default.xml')
img = cv2.imread(r'E:\cv lab\face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite('Face_Detection.jpg', img)
cv2.waitKey()