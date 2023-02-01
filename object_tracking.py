import cv2

cap = cv2.VideoCapture("mammoth.mp4")
tracker = cv2.TrackerMOSSE_create()
ret , frame = cap.read()
bbox = cv2.selectROI("track" , frame , False)
tracker.init(frame , bbox)

while True:
    ret , frame = cap.read()
    if not ret:
        break
    success , bbox = tracker.update(frame)
    if success:
        print(bbox)
        '''x , y , w , h = int(bbox[0]) , int(bbox[1]) , int(bbox[2]) , int(bbox[3])
        frame = cv2.rectangle(frame , (x , y) , (x + w , y + h) ,
                              (255 , 0 , 0) , 3)'''
    else:
        print("object Lost")
    cv2.imshow("track" , frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
