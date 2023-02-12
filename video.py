import cv2

face_Cascades = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascades_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break