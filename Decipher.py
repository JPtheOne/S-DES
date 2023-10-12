from iPerms import *
from keyGen import *
from k_Feistel import *


def decipher (ciphered_8bit, key_10bit):
    k = key_10bit
    ct = ciphered_8bit
    
    #print(f"CIPHEREDTEXT: {ct}")
    k1, k2 = subKeys_Gen(k)
    #print(f"SubKey1:{list_to_string(k1)}\nSubKey2: {list_to_string(k2)}")

    # PI, fk1, sw, fk2, IP
    ct1 = IP(ct)
    #print("IP:", list_to_string(ct1))

    f2 = feistel_Function(ct1, k2)
    #print("Feistel k2:", list_to_string(f2))

    ct2 = switchF(f2)
    #print("Switched for f2:", list_to_string(ct2))

    f1 = feistel_Function(ct2, k1)
    #print("Feistel k1:", list_to_string(f1))

    unciphered = PI(f1)
    #print(f"CIPHERED TEXT:{ct}---- UNCIPHERED:", list_to_string(unciphered))
    return unciphered


ct = "00111000"
k  = "1010000010"

print(f"Unciphered:",list_to_string(decipher(ct, k)))
