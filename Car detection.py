import cv2

original_video = cv2.VideoCapture(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\cars.mp4")
cardetectionclassifier = cv2.CascadeClassifier(r"C:\Users\parsa\Desktop\Jetlearn coding\Opencv\cars.xml")

while original_video.isOpened():
    ret, currentframe = original_video.read()
    if ret:
        grayframe = cv2.cvtColor(currentframe, cv2.COLOR_BGR2GRAY)
        cars = cardetectionclassifier.detectMultiScale(grayframe, 1.1, 1)
        for (x, y, w, h) in cars:
            cv2.rectangle(currentframe, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.imshow("Car Detection video", currentframe)
            cv2.waitKey(1)
cv2.destroyAllWindows()