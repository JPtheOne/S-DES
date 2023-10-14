from Cipher import cipher
from Decipher import decipher
from iPerms import list_to_string
from CT_and_SR import*

def str_toBin(text):
    bits = ''.join(format(ord(i), '08b') for i in text)
    return bits

def bin_toStr(binary):
    text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    return text

def fragment_Message(message):
    fragments = [message[i:i+8] for i in range(0,len(message),8)]
    return fragments

def encrypt_Text(message, key):
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



def decrypt_Text(ciphered_message, key):
    fragments = fragment_Message(ciphered_message)
    deciphered_fragments = [decipher(fragment, key) for fragment in fragments]

    deciphered_strings = [list_to_string(fragment) for fragment in deciphered_fragments]

    deciphered_binary_strings = [list_to_string(fragment) for fragment in deciphered_fragments]

    deciphered_letters = [bin_toStr(binary_string) for binary_string in deciphered_binary_strings]

    unciphered_text = list_to_string(deciphered_letters)
    return unciphered_text



if __name__ == "__main__":
    
    # VARIABLES TO CHANGE-----------------------------------------
    key = "1011110000"
    keyword ="KEY"
    message = "ok, lets go"
    print(f"To encrypt:'{message}' with key {key} for ES-DES")

    # ENCRYPT ***********************************************************
    print("----------------------------------NOW ENCRYPTING--------------------------------------")

    encrypted_message = encrypt_esDES(message, keyword)
    print("TEXTER AFTER CT & SR: ",encrypted_message)

    ciphered_bits, printable_cipher = encrypt_Text(encrypted_message, key)
    print(f"Ciphered text in bits: {printable_cipher}.\nNumber of ciphered bits: {len(printable_cipher)}, Number of ciphered bytes: {len(printable_cipher)//8}")


    # DECRYPT ***********************************************************
    print("----------------------------------NOW DECRYPTING--------------------------------------")

    decrypted_str = decrypt_Text(printable_cipher, key)
    print("DECIPHERED BUT WITH CT & SR:",decrypted_str)

    decrypted_message = decrypt_esDES(decrypted_str, keyword)
    print("Decrypted text: ", decrypted_message)