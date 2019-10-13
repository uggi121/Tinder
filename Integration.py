# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 05:04:15 2019

@author: Rahul
"""
import os
from Detect import Prediction
import cv2
from Train import Trainner

import numpy as np
import sys

from pred import main
#PUT TINDER PERSONS PICS IN test/ folder
# rubn imageProcessor
# remove images from test/ folder
def imageProcessor(folder,  filters=None):
    count = -1
    avgloss = 0
    if folder == None and filters != None:
        filters = None
    elif folder != None and filters ==None:
        folder = None
    try:
        for img in os.listdir(folder):
            #mg = cv2.imread(img)
            loss = Prediction('31').run(folder+"/"+img)
            if loss!=-1:
                if count==-1:
                    count+=1
                else:
                    count+=1
                avgloss  +=loss
              
        avgloss /= count
    except:
        print("No Particular likeable faces")
    print("before pred")
    if folder!=None:
        races = main(folder)
    flag = True
    
    try:   
        for i in filters:
            if races.count(i)>= len(races)/2:
                print("too much")
                flag = False
    except:
        print("No Ethnicity based filtering")
    
    print("after pred" , races)
    if avgloss in range(50,90) or flag:
        return True
    return False    
#if you want to train similarity checker for new dataset, uncomment the below:
#Trainner().run()
print(imageProcessor("test/",["Black"])) #ALL THE TINDER PERSON IMAGES SHOULD GO INSIDE THIS

