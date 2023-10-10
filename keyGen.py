import random

def generate_nBits(n):
    bits = ""
    for i in range(n):
        randed = random.choice('01')
        bits += randed
    return bits

def splitHalf(evenBits):
    length = len(evenBits)
    half = length//2
    l = evenBits[:half]
    r = evenBits[half:]
    return l,r

def leftShift (key, n_shifts):
    for _ in range(n_shifts):
        key = key[1:] + [key[0]]
    return key

def rightShift(key, n_shifts):
    for _ in range(n_shifts):
        key = [key[-1]] + key[:-1]
    return key

def P10 (key):
    p10_rule = [2,4,1,6,3,9,0,8,7,5]
    p10_applied = []
    
    for bit in p10_rule:
        p10_applied.append(key[bit])
    return p10_applied

def P8 (combined_key):
    p8_rule = [5,2,6,3,7,4,9,8]
    p8_applied = []

    for bit in p8_rule:
        p8_applied.append(combined_key[bit])
    return p8_applied


def subKeys_Gen(key):
    # Finding subkey 1
    p1 = P10(key)
    
    h1, h2 = splitHalf(p1)
    sh1, sh2 = leftShift(h1,1), leftShift(h2,1)

    comb1 = sh1 + sh2
    sub_Key1 = P8(comb1)

    # Finding subkey 2
    sh3, sh4 = leftShift(sh1,2), leftShift(sh2,2)
    comb2 = sh3 + sh4

    sub_Key2 = P8(comb2)

    return sub_Key1, sub_Key2


