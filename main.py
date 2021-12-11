import os
from utils import *
from generateKeys import *
from loadKeys import *
from encryption import *

keySize = 512

if os.path.exists("keys.json"):
    keys = loadKeys(keySize, JSONSaver())
    e=keys["e"]
    n=keys["n"]

    print("Sending public key: ")
    print(f"e [:100]: {str(e)[:100]}")
    print(f"n [:100]: {str(n)[:100]}")

    cipher = encrypt(e, n, "hello, world!")
    print(cipher)

else:
    keys = generateKeys(keySize, JSONSaver())
    p = keys["p"]
    q = keys["q"]
    n = keys["n"]
    e = keys["e"]
    phiN = keys["phiN"]
    peD = keys["peD"]

    print(p)
    print("\n\n\n\n")
    print(q)
    print("\n\n\n\n")
    print(n)
    print("\n\n\n\n")
    print(e)
    print("\n\n\n\n")
    print(phiN)
    print("\n\n\n\n")
    print(peD)