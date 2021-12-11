def toAscii(s:str) ->list:
    l=[]
    for i in range(len(s)):
        l.append(ord(s[i:i+1]))
    return l

def toChar(s:list) ->str:
    l=[]
    for i in range(len(s)):
        l.append(chr(s[i]))
    return l

def encrypt(e:int, n:int, msg:str) -> str:
    msg = toAscii(msg)
    cipher = []
    for i in range(len(msg)):
        cipher.append(pow(msg[i], e, n))
    return cipher

def decrypt(d:int, n:int, cipher:list):
    msg = []
    for i in range(len(cipher)):
        msg.append(pow(cipher[i], d, n))
    return msg