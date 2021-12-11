import random
from logs import *

def isCoPrime(p, q):
    """
        return True if gcd(p, q) is 1
        relatively prime
    """

    return gcd(p, q) == 1

def gcd(p, q):
    """
        euclidean algorithm to find gcd of p and q
    """

    while q:
        p, q = q, p % q
    return p

def generateE(phiN:int, keysize:int):
    # choose e
    # e is coprime with phiN & 1 < e <= phiN
    # A small public number which doesn't share a factor with phi_n and that must be odd.
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            return e

def generatePrime(keysize=2048):
    # get prime nums, p & q
    p = generateRSAPrimeNumber(log=Logs(), n=keysize)["number"]
    q = generateRSAPrimeNumber(log=Logs(), n=keysize)["number"]

    return {"p":p, "q":q}

def egcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t

def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x
 
# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]
 
def nBitRandom(n):
    return random.randrange(2**(n-1)+1, 2**n - 1)
 
def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''
    while True:
        # Obtain a random number
        pc = nBitRandom(n)
 
         # Test divisibility by pre-generated
         # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else: return pc
 
def isMillerRabinPassed(mrc, numberOfRabinTrials=20):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True

def generateRSAPrimeNumber(log=None, n:int=1024, millerInteration:int=100, failsafe:int=1000):
    c=0
    while c < failsafe:
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate, 100):
            if log != None: log.log(f"Number {str(prime_candidate)[0:10]}--- failed the Miller Rabin of {millerInteration} iterations.", "user")
            continue
        else:
            if log != None: log.log(f"Number {str(prime_candidate)[0:100]}--- passed the Miller Rabin of {millerInteration} iterations.", "root")
            return {"lenght":n, "number":prime_candidate, "message": f"The probability of this number not being prime is of 1/4^{millerInteration}.1/2^128 is the Commercial applications requirement"}

    return f"The failsafe limit ({failsafe}) has been reached. "

def generateE(phiN:int, keysize:int):
    # choose e
    # e is coprime with phiN & 1 < e <= phiN
    # A small public number which doesn't share a factor with phi_n and that must be odd.
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if (isCoPrime(e, phiN)):
            return e

def generatePrime(keysize=2048):
    # get prime nums, p & q
    p = generateRSAPrimeNumber(log=Logs(), n=keysize)["number"]
    q = generateRSAPrimeNumber(log=Logs(), n=keysize)["number"]

    return {"p":p, "q":q}