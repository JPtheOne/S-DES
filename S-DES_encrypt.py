from iPerms import *
from keyGen import *
from k_Feistel import *

pt = "10010111"
k  = "1010000010"

print(f"PLAINTEXT: {pt}")
#0. Key Generation 
k1, k2 = subKeys_Gen(k)
print(f"SubKey1:{list_to_string(k1)}\nSubKey2: {list_to_string(k2)}")

# 1. Initial Permutation
pt1 = IP(pt)
print("Initial Perm: ",list_to_string(pt1))

# 2. Apply 1st Feisel
f1 = feistel_Function(pt1, k1)
print("First Feistel: ",list_to_string(f1))

# 3. Switch halves
pt2 = switchF(f1)
print("Switching for f2: ", list_to_string(pt2))

# 4. 2nd Feistel with other half
f2 = feistel_Function(pt2, k2)
print("Second Feistel: ",list_to_string(f2))

# 5. Inverse permutation
ciphered = PI(f2)
print(f"ORIGINAL TEXT: {pt}---- CIPHERED: ",list_to_string(ciphered))
