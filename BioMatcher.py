import re
from nltk.corpus import stopwords
from textblob import TextBlob 
import cv2
import numpy as np

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

bio = """here to make new friends, just seeing da vibes and going with the flow"""

def breakSentenceToWords(input):
    input = [REPLACE_NO_SPACE.sub("", line.lower()) for line in input.split()]
    input = [REPLACE_WITH_SPACE.sub(" ", line) for line in input]
    return input

#Replace this with textblob
def validMatch(sentence, preference="pos"):
    
    dic = {"pos":0.1 , "neg":-0.1}
    threshold = dic[preference]
    blob1 = TextBlob(sentence)
    return blob1.sentiment.polarity*threshold >=0

#Replace this with tokenise
def splitSentence(input):
    input = input.split(".")
    return input

def keywordPresent(sentences, keyword, preference="pos"):
    for line in sentences:
        if keyword in line and validMatch(line, preference):
            return True
    return False

def calculatePercentage(total, keywords):
    percentage = total/len(keywords)
    return percentage * 100

def checkKeyword(bio, keywords, percentage, sentiments):
    
    parsedBio = splitSentence(bio)
    total = 0
    for idx, keys in enumerate( keywords):
        if (keywordPresent(parsedBio, keys , sentiments[idx])):
            total = total + 1
    #print(total)
    matchPercentage = calculatePercentage(total, keywords)
    #print(matchPercentage)
    if matchPercentage >= percentage:
        return True
    else:
        return False

