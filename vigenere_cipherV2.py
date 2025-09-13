def generate_vigenere_table():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vigenere_table = []
    for i in range(26):
        row = alphabet[i:] + alphabet[:i]
        vigenere_table.append(row)
    return vigenere_table

# Function to encrypt the plaintext
def encrypt(plaintext, key):
    vigenere_table = generate_vigenere_table()
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for letter in plaintext:
        if letter.isalpha():
            row = ord(key[key_index]) - 65
            col = ord(letter) - 65
            ciphertext += vigenere_table[row][col]
            key_index = (key_index + 1) % len(key)
        else:
            # modify non-alphabetic characters
            modified_char = chr((ord(letter) + ord(key[key_index])) % 26 + 65)
            ciphertext += modified_char
            key_index = (key_index + 1) % len(key)
    return ciphertext

# Function to decrypt the ciphertext
def decrypt(ciphertext, key):
    vigenere_table = generate_vigenere_table()
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0
    for letter in ciphertext:
        if letter.isalpha():
            row = ord(key[key_index]) - 65
            col = vigenere_table[row].index(letter)
            plaintext += chr(col + 97) # convert to lowercase
            key_index = (key_index + 1) % len(key)
        else:
            # modify non-alphabetic characters
            modified_char = chr((ord(letter) - ord(key[key_index])) % 26 + 65)
            plaintext += modified_char
            key_index = (key_index + 1) % len(key)
    return plaintext.lower() # convert entire plaintext to lowercase

user_input = 0     
while(user_input != ":q"):
	user_input = str(input("enter enc to encrypt and dec to decrypt and :q to exit: "))
	if user_input == "enc":
		user_plaintxt = str(input("enter PlainText: "))
		user_key = input("enter Key: ")
		print(encrypt(user_plaintxt, user_key))
	if user_input == "dec":
		user_plaintxt = str(input("enter CipherText: "))
		user_key = input("enter Key: ")
		print(decrypt(user_plaintxt, user_key))
	elif user_input != "enc" or user_input != "dec":
		pass
