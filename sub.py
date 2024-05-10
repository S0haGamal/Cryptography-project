import random
import sys 

def checkKey(key):
    return sorted(key) == list(LETTERS)
LETTERS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def getRandomkey():
    randomList=list(LETTERS)
    random.shuffle(randomList)
    return ''.join(randomList)

def EncriptionMessage(message,key):
    if (key==""):
        key = getRandomkey()
    
    if (not checkKey(key)):
        print("You Should Enter appreciate Key")    
        
    translated =''
    charsA = LETTERS
    charsB = key
    
    for symbol in message:
        if symbol.upper() in charsA:
            symIndx = charsA.find(symbol.upper())
            if symbol.isupper():
                translated +=charsB[symIndx].upper()
            else:
                translated +=charsB[symIndx].lower()
        else:
            translated+=symbol
    # print(key)
    return translated
  

def DecriptionMessage(message,key):
    translated =''
    charsA =  key
    charsB = LETTERS
    
    for symbol in message:
        if symbol.upper() in charsA:
            symIndx = charsA.find(symbol.upper())
            if symbol.isupper():
                translated +=charsB[symIndx].upper()
            else:
                translated +=charsB[symIndx].lower()
        else:
            translated+=symbol
    
    return translated         

