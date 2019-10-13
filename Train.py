# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:35:51 2019

@author: Rahul
"""

'''
This program is used to collect cropped images of a student corresponding to their student ID and train a model to suit their face.
This trained model for all the faces is stored in a trainner.yml file. 
The camera opens and takes 30 pictures when the "Get your face" button is pressed. It then crops the face and saves it in the MOONJI/data folder.
This is done using Haar Cascades, which are a very popular implementation of the Viola-Jones research paper on detecting faces in images.
Now our trainner LBPH Face recognizer trains the faces according to their student ID using LBPH face recognizer, another popular face classification algorithm

'''

#Getting the required import statements for our program and all the dependancies we need

import cv2
import numpy as np
import os
from PIL import Image
class Trainner:#The class that trains the stored images into a model
    def __init__(self):
        self.detector= cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml");#Collecting haar cascades(Though it wont be used here)
        


    def getImagesAndLabels(self, path):#the images are stored in a certain format "StudentID.ImageID.bmp". This function extracts each image
    #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #create empth face list
        faceSamples=[]
    #create empty ID list
        Ids=[]
    #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
        #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            print(imagePath)
        #getting the Id from the image
            try:
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
            except ValueError:
                print("hi")
            
        # extract the face from the training image sample
            print("lol")
            faces=self.detector.detectMultiScale(imageNp)
            print(123)
        #If a face is there then append that in the list as well as Id of it
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        return faceSamples,Ids#ID corresponds to Student ID
    def run(self):
        faces,Ids = self.getImagesAndLabels(r'Faces\data')
        recognizer = cv2.face.LBPHFaceRecognizer_create()#Creating the LPBHFaceRecognizer object to identify the face
        recognizer.train(faces, np.array(Ids))#MACHINE LEARNING. Training the recognizer to detect the faces corresponding to the ID's 
        recognizer.save('yml/trainer.yml')#Saving this in a yml file that can be read later using the same object
class FaceCropper:#This class takes 30 pictures and crops only the faces from these images and stores them as "StudentID.ImageId.bmp" in the MOONJI/data folder
    def __init__(self,Id ):
        self.samplenum = 1
        self.Id = int(Id)#Student Id
        print ('opening cam')
        self.cam =cv2.VideoCapture(0)#opens a camera. Note this can be done without opening a camera if the folder already has images
        self.detector  = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')#Opening the Haar Cascades to detect a face(NOT IDENTIFY A FACE)
    def run(self):#running the actual corpping of the face
        
        while(True):#Its a loop that breaks once 30 images are taken
    
            self.cam.open(0)
            if(self.cam.isOpened()):
    
                print ('camera is open')
       
                ret , img  = self.cam.read()#ret is a boolean that corresponds to True or false based on whether the camera has opened
                #img is the actual image the camera captures. It is a numpy array of pixels
                if ret:#If the camera successfully opens
                    print (ret)
                    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)#convert the image to grayscale to reduce processing required
                    faces = self.detector.detectMultiScale(gray, 1.3 , 5)#The function of the haarcascade that detects faces. The paremeters corresponds to the size of the face window to search and the number of adjascent features.
    
                    for(x , y , w, h ) in faces:#iterating through the face using its position and size
                        cv2.rectangle(img , (x,y) , (x+w,  y +h), (255,0,0), 2)#drawing a rectangle around it for visualization
                        self.samplenum+=1#increasing the Image ID
                        #the folder was read only, hence wouldnt work
                    isit = cv2.imwrite(r"Faces\data\User."+str(self.Id)+'.'+str(self.samplenum)+".png" , gray)#Writing it to the folder in the above format
                    isitrgb = cv2.imwrite(r"Faces\data\User."+str(self.Id)+'.'+str(self.samplenum)+"rgb.png" , img)#Writing it to the folder in the above format
                    print (isit)
                    cv2.imshow('trainer' , img)#Showing the image on a opencv window
                        
                    key = cv2.waitKey(5) #wait a few miliseconds before getting the next frame to prevent bottlenecks
                    if  key ==27 or self.samplenum >30:#quit if escape is pressed
                        break
                    
                            
        self.cam.release()#release the camera
        cv2.destroyAllWindows()#destroy the window

