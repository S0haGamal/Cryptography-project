#vignere_encryption
def vignere_encryption(msg,k):
 index=0
 length_k=len(k)
 RES=" "
 for i in range(len(msg)):
    ch=msg[i]
    if ch.isupper():
     RES+=chr((ord(ch)+ord(k[index])-65)%26+65)
     
    elif ch.islower():
      RES+=chr((ord(ch)+ord(k[index])-97)%26+97)
     
 index+=1
     
 if len(k)==length_k:
    index=0
 return RES

#vignere_decryption
 
def vignere_decryption(ciphertext,k):
 index=0
 length_k=len(k)
 RES=" "
 for i in range(len(ciphertext)):
    ch=ciphertext[i]
    if ch.isupper():
     RES+=chr((ord(ch)-ord(k[index])-65)%26+65)
     
    elif ch.islower():
      RES+=chr((ord(ch)-ord(k[index])-97)%26+97)
            
 index+=1  
    
 if len(k)==length_k:
        index=0
 return RES
