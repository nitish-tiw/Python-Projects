import cv2

captureDevice = cv2.VideoCapture(0) #captureDevice = camera

while True:
    ret, frame1 = captureDevice.read()
    ret, frame2 = captureDevice.read()
    diff = cv2.absdiff(frame1,frame2)

    cv2.imshow('Nitish Webcam', diff)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captureDevice.release()
cv2.destroyAllWindows()