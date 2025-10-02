# Input text to be encrypted
text = "Hello Talha"

# Number of positions to shift each letter
shift = 3

# Define the alphabet for encryption
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Store the encrypted result
encrypted_text = ""

# Iterate through each character in the input text
for char in text.lower():
    # Preserve spaces in the encrypted text
    if char == " ":
        encrypted_text += char
    else:
        # Find position of current character in alphabet
        index = alphabet.find(char)
        # Calculate new position after shift (wrap around using modulo)
        new_index = (index + shift) % len(alphabet)
        # Add encrypted character to result
        encrypted_text += alphabet[new_index]

print("encrypted text:", encrypted_text)
