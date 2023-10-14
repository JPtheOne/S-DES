def simple_columnar_transposition_encrypt(plaintext, keyword):
    # Removing spaces from keyword
    keyword = keyword.replace(" ", "")
    columns = len(keyword)
    rows = len(plaintext) // columns
    rows += len(plaintext) % columns

    # Adding placeholders to complete the grid, if necessary
    plaintext += '¿' * (rows * columns - len(plaintext))

    # Rearranging the columns according to the keyword
    key_order = [keyword.index(char) for char in sorted(keyword)]

    ciphertext = ''
    for index in key_order:
        ciphertext += ''.join([plaintext[row * columns + index] for row in range(rows)])
    
    return ciphertext

def simple_columnar_transposition_decrypt(ciphertext, keyword):
    keyword = keyword.replace(" ", "")
    columns = len(keyword)
    rows = len(ciphertext) // columns

    # Rearranging the columns according to the original keyword order
    key_order = [keyword.index(char) for char in sorted(keyword)]

    # Reverse mapping
    reverse_mapping = ['' * rows for _ in range(columns)]
    for index, order in enumerate(key_order):
        reverse_mapping[order] = ciphertext[index * rows: (index + 1) * rows]

    # Converting the columns back to plaintext
    plaintext = ''
    for row in range(rows):
        for column in reverse_mapping:
            plaintext += column[row]
    
    # Remove placeholder characters
    plaintext = plaintext.rstrip('¿')

    # Replace placeholder characters back to spaces
    plaintext = plaintext.replace('¿', ' ')

    return plaintext
def shift_rows(state):
    # ShiftRow for 2nd row
    state[1] = state[1][1:] + state[1][:1]
    
    # ShiftRow for 3rd row
    state[2] = state[2][2:] + state[2][:2]
    
    return state

def inv_shift_rows(state):
    # Inverse ShiftRow for 2nd row
    state[1] = state[1][-1:] + state[1][:-1]
    
    # Inverse ShiftRow for 3rd row
    state[2] = state[2][-2:] + state[2][:-2]
    
    return state



def encrypt_esDES(plaintext, keyword):
    # Step 1: Simple columnar transposition encrypt
    intermediate_text = simple_columnar_transposition_encrypt(plaintext, keyword)
    
    # Transforming intermediate text to 2D state for row shifting
    columns = len(keyword)
    rows = len(intermediate_text) // columns
    state = [list(intermediate_text[i*columns:(i+1)*columns]) for i in range(rows)]
    
    # Step 2: Shift rows
    shifted_state = shift_rows(state)
    
    # Convert state back to string
    ciphertext = ''.join([''.join(row) for row in shifted_state])
    return ciphertext

def decrypt_esDES(ciphertext, keyword):
    # Transform ciphertext into 2D state for inverse shifting rows
    columns = len(keyword)
    rows = len(ciphertext) // columns
    state = [list(ciphertext[i*columns:(i+1)*columns]) for i in range(rows)]
    
    # Step 1: Inverse shift rows
    unshifted_state = inv_shift_rows(state)
    
    # Convert state back to string
    intermediate_text = ''.join([''.join(row) for row in unshifted_state])
    
    # Step 2: Simple columnar transposition decrypt
    decrypted_text = simple_columnar_transposition_decrypt(intermediate_text, keyword)
    return decrypted_text

'''
# Example usage:
plaintext = "DID YOU SEE?"
keyword = "KEY"

# Encrypt
ciphertext = encrypt_esDES(plaintext, keyword)
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")

# Decrypt
decrypted_text = decrypt_esDES(ciphertext, keyword)
print(f"Decrypted Text: {decrypted_text}")
'''