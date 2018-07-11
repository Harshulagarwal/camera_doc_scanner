from Tkinter import *
import Tkinter as tk
from ttk import *
import cv2
import numpy as np
import tkMessageBox

root=Tk()


panedwindow = tk.PanedWindow(root, orient = VERTICAL)
panedwindow.pack(fill = BOTH, expand = False)

frame1 = tk.Frame(panedwindow, width = 100, height = 500, relief = SUNKEN)
#frame2 = tk.Frame(panedwindow, width = 400, height = 1000, relief = SUNKEN)
panedwindow.add(frame1)
#panedwindow.add(frame2)

i=np.array(1)
def up():
    str=entry.get()
    print str

    img1=cv2.imread(str)
    img1=cv2.resize(img1,(490,490),interpolation = cv2.INTER_CUBIC)
    img=cv2.GaussianBlur(img1,(3,3),3)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(gray,170,180,3)
    #ret,thresh = cv2.threshold(gray,127,255,0)
    #img1=cv2.GaussianBlur(thresh,(3,3),5)

    image, contours, hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    #img2= cv2.drawContoujpgrs(img, contours, -1, (0,255,0), 3)
    '''rect = cv2.minAreaRect(contours[0])
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    '''

    epsilon = 0.1*cv2.arcLength(contours[0],True)
    box = cv2.approxPolyDP(contours[0],epsilon,True)

    img2= cv2.drawContours(img, [box], 0, (0,255,0), 3)
    cv2.imwrite("/home/harshul/Desktop/img1.jpg",img2)
    #cv2.imwrite("/home/harshul/Desktop/img2.jpg",canny)

    i=img2
    print box

    pts1 = np.float32([box[1],box[2],box[0],box[3]])
    pts2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    dst = cv2.warpPerspective(i,M,(500,500))
    dst=cv2.flip(dst,0)
    cv2.imwrite("/home/harshul/Desktop/img.jpg",dst)

entry=tk.Entry(frame1,width=40)
entry.pack()
entry.insert(0,"path of image")


button1=tk.Button(frame1,text="upload")
button1.pack()

button1.config(justify=CENTER,font=("arial",10),width=20,command=up)

root.mainloop()
