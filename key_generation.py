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

# Test-zone ---------------------------------------------------------------------------------------------



'''
key = "1010000010"
print(f" key: {key}")

p10 = P10(key)
print(f"P10: {p10}")

h1=p10[:5:]
h2=p10[5::]
print(f"h1 = {h1} \nh2 = {h2}")

h1.append(h1.pop(0))
h2.append(h2.pop(0))

print(f"sh1: {h1} \n sh2: {h2}")

h3 = h1 + h2
print(f"Recombined halfs: {h3}")
print(f"After p8: {P8(h3)}")
'''

#https://www.geeksforgeeks.org/simplified-data-encryption-standard-key-generation/