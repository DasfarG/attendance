import cv2  # it's used for camera, capture picture and save images
from tkinter import * #it's used for create desktop Software(Desktop Application)
from tkinter import messagebox #It's used for popup messagebox
from deepface import DeepFace #it's used for compare two images if right : true, if not right: false
import dlib #It's used for Detect the faces in the image

detector = dlib.get_frontal_face_detector()

path = 'cap'
new_path = 'img'

def save(img, name):
    cv2.imwrite(name+".jpg",img)

def saves(img,name, bbox, width=300,height=300):
    x, y, w, h = bbox
    imgCrop = img[y:h, x: w]
    imgCrop = cv2.resize(imgCrop, (width, height))
    cv2.imwrite(name+".jpg", imgCrop)

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

def faces():
    frame =cv2.imread('cap1.jpg',1)
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    fit =20
    # detect the face
    for counter,face in enumerate(faces):
        print(counter)
        x1, y1 = face.left(), face.top()
        x2, y2 = face.right(), face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
        MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0, 250, 0), 3)
        saves(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit))
    frame = cv2.resize(frame,(400,400))
    cv2.imshow('Img',frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    messagebox.showinfo("Message", "Images Saved And To Click Verify For Result ")

def open():
    capture =cv2.VideoCapture(0)
    while True:
        ret,frame=capture.read()
        cv2.imshow('Face Detection',frame)
        k = cv2.waitKey(1)
        if k%256 == 32:
            save(frame,path+str(1))
            break
    messagebox.showinfo("Message","Next Frame is Selfie Image With Face detect")
    faces()
    capture.release()
    cv2.destroyAllWindows()
    

def verify():
    result = DeepFace.verify("img0.jpg","img1.jpg",model_name='Facenet')
    
    try:
        if result["verified"] == True:
            messagebox.showinfo("Message", "Happily, Face Match Is Success.")
        else:
            messagebox.showerror("Message", "Sorry, Face Match Is Failed and Try Again")
    except ValueError as e:
        messagebox.showinfo("message", e)

root=Tk()
root.geometry('700x600')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('Auto Facial Verification')
frame.config(background='light blue')
label = Label(frame, text="Auto Facial Verification",bg='black',fg='white',font=('Times 25 bold'))
label.pack(side=TOP, padx=10,pady=10)

label1 = Label(frame, text="1. To Click The Button(Open Camera) For Take Selfie with your ID.\n\n 2. Acceptable ID's - Passport, PAN Card, Driver License, Aadhar Card\n \n 3. Wait For 7 Second To Open Camera And After Open Camera, Press \n Backspace For Take Selfie and After Take The Selfie \n  With Your ID Document \n \n 4.After Face Detection Frame Is Shown, Press Any Key For\n Exit From That Frame.\n\n 5. To Click The Button(Verify) For Check Selfie Image With The Image \n Is Displayed In Their ID Document. \n\n 6. It's Take Little Bit Time For Verify The Two Image And Wait For Result. ",bg='light blue',fg='black',font=('Times 15'))
label1.pack(side=TOP, padx=10,pady=10)

but1=Button(frame,padx=5,pady=5,width=10,bg='white',fg='black',relief=GROOVE,command=open,text='Open Camera',font=('helvetica 10 bold'))
but1.pack(padx=30,pady=20)

but2=Button(frame,padx=5,pady=5,width=10,bg='white',fg='black',relief=GROOVE,command=verify,text='Verify',font=('helvetica 10 bold'))
but2.pack(padx=40,pady=30)

root.mainloop()
