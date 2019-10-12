import re
#from nltk.corpus import stopwords 

REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

bio = """My name is sudharshan. I like to fuck with people. I don't love having sex 
        and treat women like objects. I don't watch cricket. Likes soap operas."""

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

def 

 #and (not containsNegative(sentence))

def checkKeyword(bio, keyword):
    keyword = keyword.lower()
    parsedBio = splitSentence(bio)
    for sentence in parsedBio:
        words = breakSentenceToWords(sentence)
        sentence = sentence.lower()
        if ((keyword in words) and (not containsNegative(sentence))):
            return True
    return False

print(checkKeyword(bio, "SoAp OPerAs"))
