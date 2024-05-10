
def Ceaser_Encryption(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65) #This converts the shifted ASCII code back to a character by adding 65.

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result



def Ceaser_Decryption(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = 'abcdefghijklmnopqrstuvwxyz'
    final=''
    for key in range(len(LETTERS)):
        
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol) 
                new_index = (num - key) % len(LETTERS)  
                translated += LETTERS[new_index]
                
            elif symbol in letters :
                num = letters.find(symbol) 
                new_index = (num - key) % len(letters)  
                translated += letters[new_index]
                     
            else:
                translated += symbol
        final+='Hacking Key ( ' + str(key) + ' ) :'+ translated +"\n"
    return final
    

