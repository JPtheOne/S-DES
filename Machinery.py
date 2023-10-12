from Cipher import cipher
from Decipher import decipher

def str_toBin(text):
    bits = ''.join(format(ord(i), '08b') for i in text)
    return bits

message_inBits=str_toBin("Puto el que lo lea")
print(f"Message in bits:{ message_inBits}, bits:",len(message_inBits))

def fragment_Message(message):
    fragments = [message[i:i+8] for i in range(0,len(message_inBits),8)]
    return fragments

fragments = fragment_Message(message_inBits)
print("Fragments: ",fragments)


key = "1010000010"

# Apply the cipher function to each fragment
ciphered_fragments = [cipher(fragment, key) for fragment in fragments]
print("Ciphered Fragments:", ciphered_fragments)



# Now, to decrypt, apply the decipher function to each ciphered fragment
deciphered_fragments = [decipher(fragment, key) for fragment in ciphered_fragments]
print("Deciphered Fragments:", deciphered_fragments)

