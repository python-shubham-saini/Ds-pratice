import cv2
import os
import numpy as np
from tkinter import * 
import tkinter as tk
from tkinter.filedialog import *
from pathlib import Path
# from PIL import Image
# from matplotlib import pyplot as plt
import time
tim = time.time_ns()

# try:
#     outpur_dir = os.mkdir('OUTPUT')
# except:
#     print("Directory alreafy exist")

def readFile(isGrey = 1):
    global file
    file = askopenfilename(filetypes =[('Image File',['.jpeg', '.jpg', '.png'])])
    try :
        img = cv2.imread(file, isGrey)
        return img
    except :
        print('Plese Select Image')

def saveImage(img, modifiedImg, opName="imgtransform"):
    try:
        res = np.hstack((img, modifiedImg)) 
        
        targetFileName = (Path(file)).stem + "_" + str(tim) + "_" + opName  + (Path(file)).suffix  
        print(targetFileName)
        cv2.imwrite(targetFileName, res)
        Image.open(targetFileName).show()

        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)

class Pointprocessing():
    def imageNegative():

        img = readFile()
        modifiedImg = cv2.bitwise_not(img)
        saveImage(img, modifiedImg, "img_negative")     

    def contrastStreching():
        img = readFile()      
        xp = [0, 64, 128, 192, 255]
        fp = [0, 16, 128, 240, 255]
        x = np.arange(256)
        table = np.interp(x, xp, fp).astype('uint8')
        modifiedImg = cv2.LUT(img, table)
        saveImage(img , modifiedImg,'contrastStreching')

    def histrogramEqualization():
        img = readFile(0) 
        modifiedImg = cv2.equalizeHist(img)
        saveImage(img, modifiedImg,'histrogramEqualization') 

    def powerLow():
        img = readFile()
        powerlow_level= float(pl)
        gamma_two_point_two = np.array(255*((img/255)**powerlow_level),dtype='uint8')
        modifiedImg1 = cv2.hconcat([gamma_two_point_two])
        saveImage(img ,modifiedImg1,'powerLow')

    def intensitylevelslicing():
        img = readFile(0)
        row, column = img.shape
        modifiedImg = np.zeros((row,column),dtype = 'uint8')
        min_range = int(intensity_lvl_min)
        max_range = int(intensity_lvl_max)
        for i in range(row):
            for j in range(column):
                if img[i,j]>min_range and img[i,j]<max_range:
                    modifiedImg[i,j] = 255
                else:
                    modifiedImg[i,j] = 0
        saveImage(img, modifiedImg,'intensitylevelslicing')

class Neighborhoodprocessing():
    def imageSmoothing():
        img = readFile()
        x = int(imgsmth_x)
        y = int(imgsmth_y)
        modifiedImg = cv2.blur(img, (x,y))
        saveImage(img, modifiedImg , 'imageSmoothing')

    def gaussian():
        img = readFile()
        modifiedImg = cv2.GaussianBlur(img,(int(gussimg_x),int(gussimg_y)),0)
        saveImage(img, modifiedImg,'gaussian')

    def median():
        img = readFile()
        median_number=int(mi)
        modifiedImg = cv2.medianBlur(img,median_number)
        saveImage(img, modifiedImg,'median')

    def laplacian():
        img = readFile()
        modifiedImg = cv2.Laplacian(img, cv2.CV_64F)
        saveImage(img, modifiedImg,'laplacian') 

    def highboost():
        img = readFile()
        highbooost= int(hi)
        kernel = np.array([[-1, -1, -1],
                        [-1,  highbooost, -1],
                        [-1, -1, -1]])
        modifiedImg = cv2.filter2D(img, -1, kernel)
        saveImage(img , modifiedImg,'highboost')
        
#<-=-==-=-=-=-=-=-=-==-=-=-=-======-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=>
main = Tk()
main.title("Image transformation")
# main.iconbitmap()
# main.geometry('600x600')
ID=IntVar()
lvl1 = Label(main, text = "Level :") 
lvl2 = Label(main, text = "Level :") 
lvl3 = Label(main, text = "Level :") 

box1=Entry(main,bd=4,textvariable=ID)
box2=Entry(main,bd=4,textvariable=ID)
box3=Entry(main,bd=4,textvariable=ID)

box1.grid(pady=5,row=5,column=2)
lvl1.grid(row=5,column=1) 
box2.grid(pady=5,row=10,column=2)
lvl2.grid(row=10,column=1) 
box3.grid(pady=5,row=12,column=2)
lvl3.grid(row=12,column=1) 

pl = box1.get()
mi = box2.get()
hi = box3.get()

min_label = Label(main, text = "Minimum :") 
intensity_lvl_min1 = Entry(main,bd=4,textvariable=ID)
max_label = Label(main, text = "Maximum :") 
intensity_lvl_max1 = Entry(main,bd=4,textvariable=ID)

intensity_lvl_min1.grid(pady=5,row=6,column=2)
min_label.grid(pady=5,row=6,column=1)

intensity_lvl_max1.grid(pady=5,row=6,column=4)
max_label.grid(pady=5,row=6,column=3)

intensity_lvl_min = intensity_lvl_min1.get()
intensity_lvl_max = intensity_lvl_max1.get()

x1_cordinate=Entry(main,bd=4,textvariable=ID)
x1_label = Label(main, text = "X-Coordinate :") 
x2_cordinate=Entry(main,bd=4,textvariable=ID)
x2_label = Label(main, text = "X-Coordinate :") 
y1_cordinate=Entry(main,bd=4,textvariable=ID)
y1_label = Label(main, text = "Y-Coordinate :") 
y2_cordinate=Entry(main,bd=4,textvariable=ID)
y2_label = Label(main, text = "Y-Coordinate :")

x1_cordinate.grid(pady=5,row=8,column=2)
x1_label.grid(pady=5,row=8,column=1)
y1_cordinate.grid(pady=5,row=8,column=4)
y1_label.grid(pady=5,row=8,column=3)
x2_cordinate.grid(pady=5,row=9,column=2)
x2_label.grid(pady=5,row=9,column=1)
y2_cordinate.grid(pady=5,row=9,column=4)
y2_label.grid(pady=5,row=9,column=3)

imgsmth_x = x1_cordinate.get()
imgsmth_y = y1_cordinate.get()

gussimg_x = x2_cordinate.get()
gussimg_y = y2_cordinate.get()


l1 = Label(main, text = "Point Processing") 
l1.config(font =("Courier", 14))
b1 = Button(main, text = "Image Negative", command=lambda: Pointprocessing.imageNegative()) 
b2 = Button(main, text = "Contrast Streching", command=lambda: Pointprocessing.contrastStreching()) 
b3 = Button(main, text = "HistrogramEqualization", command=lambda: Pointprocessing.histrogramEqualization()) 
b4 = Button(main, text = "Power Low (Level)", command=lambda : Pointprocessing.powerLow()) 
b5 = Button(main, text = "Intensity level slicing (Min, Max)", command=lambda: Pointprocessing.intensitylevelslicing()) 

l1.grid(pady=5,row=1 ,column=0) 
b1.grid(pady=5,row=2,column=0)
b2.grid(pady=5,row=3,column=0)
b3.grid(pady=5,row=4,column=0)
b4.grid(pady=5,row=5,column=0)
b5.grid(pady=5,row=6,column=0)

l2 = Label(main, text = "Neighborhood processing") 
l2.config(font =("Courier", 14))
b1 = Button(main, text = "Image Smoothing (Coordinate)", command=lambda: Neighborhoodprocessing.imageSmoothing()) 
b2 = Button(main, text = "Gaussian Image (Coordinate)", command=lambda: Neighborhoodprocessing.gaussian()) 
b3 = Button(main, text = "Median Image (Level) ", command= lambda:  Neighborhoodprocessing.median()) 
b4 = Button(main, text = "Laplacian Sharapnning Image", command=lambda: Neighborhoodprocessing.laplacian()) 
b5 = Button(main, text = "Highboost  Image (Level)", command=lambda: Neighborhoodprocessing.highboost()) 

l2.grid(pady=5,row=7 ,column=0) 
b1.grid(pady=5,row=8,column=0)
b2.grid(pady=5,row=9,column=0)
b3.grid(pady=5,row=10,column=0)
b4.grid(pady=5,row=11,column=0)
b5.grid(pady=5,row=12,column=0)

b2 = Button(main, text = "Exit",command = main.destroy)  
b2.grid(pady=5,row=13,column=0)

main.mainloop()
