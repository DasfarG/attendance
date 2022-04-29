import cv2
from tkinter import *
from PIL import Image,ImageTk
import face_recognition



"""
def open():
    image = Image.fromarray(img1)
    time = str(datetime.datetime.now().today()).repalce(":"," ")+".png"
    image.save(time)
 """
img_counter = 0



#def Face():
   
def Photo():
    k = cv2.waitKey(1)
    global img_counter
    if k%256 == 27:
        # press esc
        print("Escape hit, closing...")
        #break
    else:
        # press space
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, img1)
        print("{} written!".format(img_name))
        print(matches)
        img_counter += 1  
"""
def Myframe(self):
    #y1,x2,y2,x1 = faceLoc
    cv2.rectangle(img1,(x1,y1),(x2,y2),(255,0,0),2)
"""
root = Tk()
root.geometry("700x640")
root.configure(bg="black")
Label(root,text="Halley Test", font=("times new roman",30,"bold"),bg="black",fg="red").pack()
f1 = LabelFrame(root,bg="red")
f1.pack()
L1 = Label(f1,bg="red")
L1.pack()
cap = cv2.VideoCapture(0)
Button(root,text="Take Snapshot",font=("times new roman",30,"bold"),bg="black",fg="red",command=Photo).pack(fill=X,expand=True,pady=20)


def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =2):
    """To draw stylish rectangle around the objects"""
    cv2.line(rgb, (x,y),(x+v,y), color, thikness)
    cv2.line(rgb, (x,y),(x,y+v), color, thikness)

    cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
    cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

    cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
    cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

    cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
    cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)


    
    
while True:
    ret, img = cap.read()
    if not ret:
        print("failed to grab frame")
        break
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    faceLoc = face_recognition.face_locations(img1)
    encodeCurFrame = face_recognition.face_encodings(img1,faceLoc)
    for encodeFace, faceLoc in zip(encodeCurFrame,faceLoc):
        matches = face_recognition.compare_faces(encodeCurFrame, encodeFace)
        #print(matches)
        y1,x2,y2,x1 = faceLoc
        #y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
        cv2.rectangle(img1,(x1,y1),(x2,y2),(255,0,0),2)
        #Myframe(img1,(x1, y1), (x2 , y2),(0, 255, 0), 2)
        


        
    #cv2.imshow('test',img1)    
       
    
root.update()
    
cap.release()