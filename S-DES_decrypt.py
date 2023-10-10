from iPerms import *
from keyGen import *
from k_Feistel import *

ct = "00111000"
k1 = "10100100"
k2 = "01000011"

# PI, fk1, sw, fk2, IP
ct1 = IP(ct)
print("IP:", list_to_string(ct1))

f2 = feistel_Function(ct1, k2)
print("Feistel k2:", list_to_string(f2))

ct2 = switchF(f2)
print("Switched for f2:", list_to_string(ct2))

f1 = feistel_Function(ct2, k1)
print("Feistel k1:", list_to_string(f1))

unciphered = PI(f1)
print("Unciphered:", list_to_string(unciphered))