import cv2
import face_recognition

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    
    faceLoc = face_recognition.face_locations(frame)
    encodeCurFrame = face_recognition.face_encodings(frame,faceLoc)
    for encodeFace,faceLoc in zip(encodeCurFrame,faceLoc):
        matches = face_recognition.compare_faces(encodeCurFrame, encodeFace)
        
        #print(matches)
        y1,x2,y2,x1 = faceLoc
        #y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # press esc
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # press space
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        print('It is a match',matches)
        img_counter += 1
cam.release()
cv2.destroyAllWindows()
