from iPerms import *
from keyGen import *
from k_Feistel import *



def decrypt(ciphertext, k1, k2):
    # 1. Initial Permutation
    pt1 = IP(ciphertext)
    print("Initial Perm: ", pt1)
    
    # 2. Apply 1st Feistel with k2
    f1 = feistel_Function(pt1, k2)
    #print("First Feistel: ", f1)
    
    # 3. Switch halves
    pt2 = switchF(f1)
    #print("Switching for f2: ", pt2)
    
    # 4. 2nd Feistel with k1
    f2 = feistel_Function(pt2, k1)
    #print("Second Feistel: ", f2)
    
    # 5. Inverse permutation
    decrypted = PI(f2)    
    return list_to_string(decrypted)


ct = "00111000"
k1 = "10100100"
k2 = "01000011"

print(decrypt(ct,k1,k2))
'''
ct1 = PI(ct)
f2 = feistel_Function(ct1, k2)
ct2 = switchF(f2)
f1 = feistel_Function(ct2, k1)
unciphered = IP(f1)

print("Unciphered is: ", list_to_string(unciphered))
'''