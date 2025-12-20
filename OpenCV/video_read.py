import cv2

video = cv2.VideoCapture("Galaxy.mp4")

while video.isOpened():
    _, frame = video.read()

    frame = cv2.resize(frame, (800,720))

    cv2.imshow("Ouotput", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()