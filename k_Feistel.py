
def get_S(half, s):
    
    S0 = [
        [1, 0, 3, 2],
        [3, 2, 1, 0],
        [0, 2, 1, 3],
        [3, 1, 3, 2]
        ]

    S1 = [
        [0, 1, 2, 3],
        [2, 0, 1, 3],
        [3, 0, 1, 0],
        [2, 1, 0, 3]
        ]

    if s==0:
        S = S0
    elif s==1:
        S = S1

    row = half[0] + half[-1]
    col = half[1] + half[2]

    i = int(row,2)
    j = int(col,2)

    s_value = S[i][j]
    bin_s = bin(s_value)

    return bin(s_value)[2:].zfill(2)

def EP(half):
    EP_rule = [3,0,1,2,1,2,3,0]
    EPermuted = []
    for bit in EP_rule:
        EPermuted.append(half[bit])
    return EPermuted

def P4(half):
    P4_rule = [1,3,2,0]
    P4_applied = []
    for bit in P4_rule:
        P4_applied.append(half[bit])
    return P4_applied

def XOR (n1, n2):
    str_n1 = ''.join(str(bit) for bit in n1)
    str_n2 = ''.join(str(bit) for bit in n2)

    n1 = int(str_n1,2)
    n2 = int(str_n2,2)
    r = bin(n1^n2)

    xor_result = r[2:].zfill(len(str_n1))
    return list(xor_result)

def splitHalf(evenBits):
    length = len(evenBits)
    half = length//2
    l = evenBits[:half]
    r = evenBits[half:]
    return l,r

def switchF(bit8_key):
    l,r = splitHalf(bit8_key)
    switched = r + l
    return switched

def feistel_Function(plaintext, key_n):
    l1, r1 = splitHalf(plaintext)       # 2. Divide on halves
    ep1 = EP(r1)                        # 3. Apply EP on r half
    x1 = XOR(key_n, ep1)                 # 4. key XORed with EP
    l2, r2 = splitHalf(x1)              # 5. Split XORed
    s0, s1 = get_S(l2,0), get_S(r2,1)   # 6. Use halves to seek on S-Boxes
    comb_S = s0 + s1                    # 7. Recombine S founds
    s_p4 = P4(comb_S)                   # 8. Apply P4 on full S
    x2 = XOR(l1, s_p4)                  # 9. L1 with P4 Xored
    last_Comb = ''.join(x2) + ''.join(r1)                 # 10. Recombine Xored with r1
    return last_Comb


