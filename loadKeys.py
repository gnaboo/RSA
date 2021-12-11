from utils import *

def loadKeys(keySize:int, jsoninstance) ->dict:

    with open(jsoninstance.name, "r") as f:
        content = json.loads(f.read())

    p = content["p"]
    q = content["q"]
    n = content["n"]
    e = content["e"]
    phiN = content["phiN"]
    peD = content["peD"]

    return {"p":p, "q":q, "n":n, "phiN":phiN, "e":e, "peD":peD}