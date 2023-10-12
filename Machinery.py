from Cipher import cipher
from Decipher import decipher
from iPerms import list_to_string

def str_toBin(text):
    bits = ''.join(format(ord(i), '08b') for i in text)
    return bits

def bin_toStr(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def fragment_Message(message):
    fragments = [message[i:i+8] for i in range(0,len(message),8)]
    return fragments

def encrypt_text(message, key):
    #print("To encrypt: ", message_toEncrypt)
    message_inBits=str_toBin(message)
    #print(f"Message in bits:{ message_inBits}, bits:",len(message_inBits))

    fragments = fragment_Message(message_inBits)
    #print("Fragments: ",fragments)

    ciphered_fragments = [cipher(fragment, key) for fragment in fragments]
    ciphered_strings = [list_to_string(fragment) for fragment in ciphered_fragments]
    ciphered_text = list_to_string(ciphered_strings)
    #print("Ciphered Strings:", ciphered_strings)
    return ciphered_fragments, ciphered_text

def decrypt_Text(ciphered_fragments, key):
    deciphered_fragments = [decipher(fragment, key) for fragment in ciphered_fragments]
    deciphered_strings = [list_to_string(fragment) for fragment in deciphered_fragments]
    #print("Deciphered strings: ", deciphered_strings)

    deciphered_binary_strings = [list_to_string(fragment) for fragment in deciphered_fragments]
    deciphered_letters = [bin_toStr(binary_string) for binary_string in deciphered_binary_strings]

    unciphered_text = list_to_string(deciphered_letters)
    return unciphered_text

# Test zone----------------------------------------------------------
key = "1010000010"
message = "The enemy has amassed a considerable force. POSSIBLE INCOMING ATTACK"
print("Message to encrypt: ", message)

ciphered_bits, printable_cipher = encrypt_text(message, key)
print(f"Ciphered text in bits: {printable_cipher}.\nNumber of ciphered bits: {len(printable_cipher)}, Number of ciphered bytes: {len(printable_cipher)//8}")

unciphered_Text = decrypt_Text(ciphered_bits, key)
print("Unciphered Text: ", unciphered_Text)
