#Rot13_encryption
def Rot13_encryption(text):
    rot13trans=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                         'NOPQRSTUVWXYZABCDEFGHIJKLMNOPQrstuvwxyzabcdefghijklm')
    Res=text.translate(rot13trans)
    return Res





def Rot13_decryption(text):
    rot13trans=str.maketrans('NOPQRSTUVWXYZABCDEFGHIJKLMNOPQrstuvwxyzabcdefghijklm',
                         'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    Res=text.translate(rot13trans)
    return Res

