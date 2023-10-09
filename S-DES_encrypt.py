from iPerms import *
from keyGen import *
from k_Feistel import *


pt = "10010111"
k1 = "10100100"
k2 = "01000011"

# 1. Initial Permutation
pt1 = IP(pt)
#print("Initial Perm: ",pt1)

# 2. Apply 1st Feisel
f1 = feistel_Function(pt1, k1)
#print("First Feistel: ",f1)

# 3. Switch halves
pt2 = switchF(f1)
#print("Switching for f2: ", pt2)

# 4. 2nd Feistel with other half
f2 = feistel_Function(pt2, k2)
#print("Second Feistel: ",f2)

# 5. Inverse permutation
ciphered = PI(f2)
print("Ciphered is: ",list_to_string(ciphered))
