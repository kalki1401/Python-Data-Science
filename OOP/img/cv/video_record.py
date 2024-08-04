import cv2
video=cv2.VideoCapture(0) #webcam
codec=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('output.mp4',codec,20.0,(640,480))
while True:
    status,frame=video.read()
    # frame = cv2.resize(frame, (0,0), fx=.1, fy=.1)
    # print(status,frame)
    if not status:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output.write(gray)
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(1)==27:
        break
video.release()
output.release()
cv2.destroyAllWindows()