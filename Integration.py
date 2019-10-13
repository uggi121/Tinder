# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 05:04:15 2019

@author: Rahul
"""
import os
from Detect import Prediction
import cv2
from Train import Trainner
from BioMatcher import checkKeyword
import numpy as np
import sys

from pred import main
#PUT TINDER PERSONS PICS IN test/ folder
# rubn imageProcessor
# remove images from test/ folder
def imageProcessor(folder,counter):
    filters=open("matching/filter"+str(counter)+".txt",  "r")
    filters = filters.readline().strip().split()
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
def TextProcessor(counter):
    text = open("matching/textfilter"+str(counter)+".txt" ,"r")
    bio=""
    keywords =[]
    flag = True
    sentiment = []
    for line in text:
        if line.s trip() != "#####"and flag:
            bio+=line.strip()+" . "
        elif line.strip() == "#####":
             flag = False
        elif line.strip() != "#####" and not flag and line!="\n":
                #print(line)
                keywords.append(line.strip().split()[0])
                sentiment.append(line.strip().split()[1])
                
    text.close()
    print(keywords)
    print(bio)
    return(checkKeyword(bio, keywords, 80 , sentiment ))
        
            
            
    
#if you want to train similarity checker for new dataset, uncomment the below:
#Trainner().run()
f = open("rightswipe.txt","w")
g = open("leftswipe.txt" , "w")
for i in range(1, 5):
    
    result = (imageProcessor("testt/profile"+str(i), i) and TextProcessor(i)) #ALL THE TINDER PERSON IMAGES SHOULD GO INSIDE THIS
    print(result)
    
    if result==True:
        f.write("profile"+str(i)+"\n")
    else:
        g.write("profile"+str(i)+"\n")
f.close()
g.close()

