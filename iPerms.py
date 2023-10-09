
def IP(plaintext):
    IP_rule = [1,5,2,0,3,7,4,6]
    IPermuted = []
    for bit in IP_rule:
        IPermuted.append(plaintext[bit])
    return IPermuted

def PI(plaintext):
    PI_rule = [3,0,2,4,6,1,7,5]
    PI_permuted = []
    for bit in PI_rule:
        PI_permuted.append(plaintext[bit])
    return PI_permuted

def list_to_string(list):
    return ''.join(list)


'''
#--Testing zone---------------------------------------------
plaintext = "01011111"
print("Original msg: ", list(plaintext))

init_Permuted = IP(plaintext) 
print("Plaintext to IP: ", init_Permuted)

inv_Permuted = PI(init_Permuted)
print("IP to Plaintext ",inv_Permuted)
'''