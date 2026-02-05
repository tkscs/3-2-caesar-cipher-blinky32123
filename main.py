import string
import random

# ----- Some Hints -----
# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase
print(f"{alphabet = }")

# You can look up the index of a letter in the alphabet like this:
#index = alphabet.index("a")
#print(f"position of 'a' in the alphabet: {index}")
# The computer already thinks of all the characters it can print out as numbers.
# If you want to, you can look up what number a character corresponds to in
# "ASCII" encoding: 
#ascii_number = ord("a")
#print(f"ascii number representation of 'a': {ascii_number}")

#ascii_letter = chr(97)
#print(f"ascii letter at position #97: {ascii_letter}")

# ----- Your Algorithm -----
# Your task is to encrypt this secret message into ciphertext
plaintext = "This is a secret message."

# Initialize your ciphertext an empty string
ciphertext = ""
encrypted_character = ""
for character in plaintext:

    # do something to the character to encrypt it
    
    ascii_number = ord(character)
    ascii_number = ascii_number + 10
    encrypted_character = chr ( ascii_number)

    ciphertext += encrypted_character

print(f"{ciphertext = }")

character = ""
decrypted_character = ""
deciphertext = ""

for character in ciphertext:
    # do something to the character to decrypt it
    ascii_number = ord(character)
    ascii_number = ascii_number - 10
    decrypted_character = chr ( ascii_number)

    deciphertext += decrypted_character

print(f"{deciphertext = }")

# alphabet, a=0 t=19 h=7 i=9 s=18 e=4 c=2 r=19 m=12 g=6 
#ascii a=97 t h i s e c r m g 








def plaintext_randomizer():
    left_ciphertext=""
    right_ciphertext=""
    for character in plaintext:
        if ...:
            left_ciphertext+=character
        else: 
            left_ciphertext+=character



