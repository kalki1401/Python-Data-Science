import cv2
video=cv2.VideoCapture(r"C:\Users\DELL\Downloads\4823938-uhd_2160_3840_24fps.mp4")
while True:
    status,frame=video.read()
    frame = cv2.resize(frame, (0,0), fx=.1, fy=.1)
    print(status,frame)
    if not status:
        break
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(1)==27:
        break
video.release()
cv2.destroyAllWindows()