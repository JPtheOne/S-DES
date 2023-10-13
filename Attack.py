from Machinery import*

def bruteForce_Attack(original_message, ciphered_msg):
    # Create the ciphered_msg by encrypting the ciphered_msg with the given key
    
    possible_keys = [format(i, '0' + str(10) + 'b') for i in range(2**10)]

    for i, possible_key in enumerate(possible_keys):
        decrypted_msg = decrypt_Text(ciphered_msg, possible_key)  # Assuming there's a decrypt function in Machinery
        if decrypted_msg == original_message:
            print(f"Lock broken at test {i} from {len(possible_keys)}: {possible_key}")
            break 
    return possible_key

'''
original_message = "ok, lets go"
encrypted_message = "1001110011111001010000010001101111010101110011011000011111111100000110111101001010011100"

print(bruteForce_Attack(original_message, encrypted_message))
'''