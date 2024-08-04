import cv2
video=cv2.VideoCapture(r"C:\Users\DELL\Downloads\4823938-uhd_2160_3840_24fps.mp4")
while True:
    status,frame=video.read()
    frame = cv2.resize(frame, (0,0), fx=.1, fy=.1)
    print(status,frame)
    if not status:
        break
    #make changes from this line
    newframe=frame*10
    bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rgb= bw=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("Video Frame",frame)
    cv2.imshow("New Video Frame",newframe)
    cv2.imshow("B/W",bw)
    cv2.imshow("rgb",rgb)
    if cv2.waitKey(1)==27:
        break
video.release()
cv2.destroyAllWindows()