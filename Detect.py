# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 13:19:27 2019

@author: Rahul
"""

'''
This program authenticates the user. Authentication refers to whether the Authorized user is the said user. 
While authorization is whether the person is enabled access.
Our program first authorizes a student ID. Then authenticates the face to a student ID. If the Student ID is authorized, the door is unlocked
'''
#Picking all the required import statements
import cv2
import numpy as np

class Prediction():#Our prediction class reads the previously trained yml file and applies it to the image being read and confirms identity corresponding to Student ID
    def __init__(self, studid):#Constructor that takes in the Student ID. This will be passed through the Text Input in our gui
        self.studid = studid#class variable initialized to constructor parameter
        self.cam = cv2.VideoCapture(0) #Initializing a camera       
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()#Creating a LBPH face recognizer object that will read our yml file
       # self.detection_model_path = 'haarcascade_frontalface_default.xml'#HaarCascades are used to detect a face in an image. The face identification is applied on this detected face
        try:
            self.recognizer.read('yml/trainer.yml')#Reading the yml file that contains all the trained faces
            print("....yml file loaded")
        except:
            print("###No trainer file detected")
        try:  
            self.cascadePath = "cascades/haarcascade_frontalface_default.xml"#HaarCascades are used to detect a face in the image and the face identification is applied on this detected face
            self.faceCascade = cv2.CascadeClassifier(self.cascadePath)#Setting the cascade classifier to our haar cascade
            print("...cascade loaded")
        except:
            print("###No cascade detected")
        
        self.counter = 0#Counter to count the number of times the face has been detected
    def run(self,im=""):#Method that takes care of the actual prediction
        if im!="":
            conf=0
            im = cv2.imread(im)
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#Converting the image to greyscale for less processing requirements as greyscale is single channel while RGP is three channels
            faces=self.faceCascade.detectMultiScale(gray, 1.2,5)#Detecting the face based on the haard cascade from the grey image. NOTE: COLOR DOES NOT AFFECT FACE DETECTION. The parameters correspond to the number of nearby features to be detected and the size of the window to scan for a face
            conf = -1
            for(x,y,w,h) in faces:#iterating through the positional pixels and width height of the face
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)#Drawing a rectangle for visualization purposes
                Id, conf = self.recognizer.predict(gray[y:y+h,x:x+w])#using the LBPH Face Recognizer binded to the yml file to predict the face to its student ID.
                #ID returns the student ID of the face and conf returns the confidence of the prediction
                 
                print("confidence is : " , conf)
                
                    # cv2.PutText(im, str(Id), (x, y+h) , font, 1 , (0,255,0) )
            cv2.imshow('recognizer',im) #Showing the detection process on screen using an opencv window
            
        
            self.cam.release()#release the camera from the program
            cv2.destroyAllWindows()#destory all the active opencv windows
            return conf
        while True:#USes a loop that breaks once the authorized face has been identified 3 times in a row, leading to unlock
            ret, im =self.cam.read()#reading from the camera. ret is a boolean that tells us if the image is read. im is the actual image
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)#Converting the image to greyscale for less processing requirements as greyscale is single channel while RGP is three channels
            faces=self.faceCascade.detectMultiScale(gray, 1.2,5)#Detecting the face based on the haard cascade from the grey image. NOTE: COLOR DOES NOT AFFECT FACE DETECTION. The parameters correspond to the number of nearby features to be detected and the size of the window to scan for a face
            
            for(x,y,w,h) in faces:#iterating through the positional pixels and width height of the face
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)#Drawing a rectangle for visualization purposes
                Id, conf = self.recognizer.predict(gray[y:y+h,x:x+w])#using the LBPH Face Recognizer binded to the yml file to predict the face to its student ID.
                #ID returns the student ID of the face and conf returns the confidence of the prediction
                 
                print("confidence is : " , conf)
                if str(Id) == self.studid:#IF the student ID detected is the student ID to be authenticated, then increment counter
                    print("Check")
                    self.counter +=1
                    if self.counter>=3:#If the same face has been detected 3 times, succeessfully unlock the door
                        print("Successfully unlocked")
                        break
                             
                else:#If the student ID detected is not the one to be authenticated, then ID = "Unknown"
                    #Id="Unknown"
                    pass
                    #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
                print(str(Id))
                    # cv2.PutText(im, str(Id), (x, y+h) , font, 1 , (0,255,0) )
            cv2.imshow('recognizer',im) #Showing the detection process on screen using an opencv window
            if cv2.waitKey(20) & 0xFF==ord('q'):#wait a few seconds/miliseconds until the camera sends the next image to prevent lag/bottlenecks. IF q is pressed, break
                break
        self.cam.release()#release the camera from the program
        cv2.destroyAllWindows()#destory all the active opencv windows

#ow to Prediction("21221" ).run()
