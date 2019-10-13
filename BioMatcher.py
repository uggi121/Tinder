import re
#from nltk.corpus import stopwords 

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

bio = """here to make new friends, just seeing da vibes and going with the flow"""

def breakSentenceToWords(input):
    input = [REPLACE_NO_SPACE.sub("", line.lower()) for line in input.split()]
    input = [REPLACE_WITH_SPACE.sub(" ", line) for line in input]
    return input

#Replace this with textblob
def containsNegative(sentence):
    if ("don't" in sentence):
        return True
    return False

#Replace this with tokenise
def splitSentence(input):
    input = input.split(".")
    return input

def keywordPresent(sentences, keyword):
    for line in sentences:
        if keyword in line and not containsNegative(line):
            return True
    return False

def calculatePercentage(total, keywords):
    percentage = total/len(keywords)
    return percentage * 100

def checkKeyword(bio, keywords, percentage):
    keywords = keywords.lower().split(", ")
    parsedBio = splitSentence(bio)
    total = 0
    for keys in keywords:
        if (keywordPresent(parsedBio, keys)):
            total = total + 1
    print(total)
    matchPercentage = calculatePercentage(total, keywords)
    print(matchPercentage)
    if matchPercentage >= percentage:
        return True
    else:
        return False

print(checkKeyword(bio, "friend", 60))
