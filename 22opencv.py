import cv2

if __name__ == '__main__':
    img = cv2.imread('./people.jpg')



    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = classifier.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('lyy', img)
    cv2.waitKey(0)
