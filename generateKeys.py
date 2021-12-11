import random
from utils import *

def generateKeys(keySize:int, jsoninstance) ->bool:

    keys = generatePrime(keySize)
    p = keys["p"] # P, a prime number generated randomly and checked using Miller Rabin's algorithm.
    q = keys["q" ]# Q, a prime number generated randomly and checked using Miller Rabin's algorithm.

    n = p * q # N, a public number which's phi will be used in D, the private exponant;

    phiN = (p - 1) * (q - 1) # Phi of N (noted Φn) can be easily calculated if p and q are know. This is the private value allowing the decryption;

    e = generateE(phiN, keySize) # e, a random, odd number that doesn't share a factor with Phi of N.

    # choose d
    # D is Modular Inversion of e with respect to phiN, e * d (mod phiN) = 1
    peD = modularInv(e, phiN)

    values = {"p":p, "q":q, "n":n, "phiN":phiN, "e":e, "peD":peD}

    jsoninstance.save(values)

    return values
