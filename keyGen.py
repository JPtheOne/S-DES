import random

def generate_nBits(n):
    bits = ""
    for i in range(n):
        randed = random.choice('01')
        bits += randed
    return bits

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

'''
# Test-zone ---------------------------------------------------------------------------------------------
key = "1010000010"
print(f" key: {key}")

p10 = P10(key)
print(f"P10: {p10}")

h1=p10[:5:]
h2=p10[5::] 
print(f"h1 = {h1} \nh2 = {h2}")

sh1 = leftShift(h1, 1)
sh2 = leftShift(h2, 1)

print(f"sh1: {sh1} \n sh2: {sh2}")

comb1 = sh1 + sh2
print(f"Recombined halfs: {comb1}")
k1 = P8(comb1)
print(f"After p8: {k1}")

# for k2
sh3 = leftShift(sh1,2)
sh4 = leftShift(sh2,2)

print(f"2 bit LS, result on: \nsh3: {sh3} \nsh4:{sh4}")

comb2 = sh3 + sh4
print("Recombined halfs: ", comb2)

k2 = P8(comb2)

print("K1: " + "".join(k1))
print("K2: " + "".join(k2))
#https://www.geeksforgeeks.org/simplified-data-encryption-standard-key-generation/
'''