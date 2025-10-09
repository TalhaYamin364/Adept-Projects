# Caesar cipher example
"""
Simple Caesar cipher example.

This module encrypts a hard-coded string using a Caesar cipher
that shifts letters by a fixed amount. It exists to demonstrate
a minimal encryption example and to satisfy Pylint's requirement
for a module-level docstring (C0114).
"""


# Input text to be encrypted
def main() -> str:
    """Encrypt a hard-coded message with a simple Caesar cipher and print it.

    Keeping variables as local names avoids module-level constant naming
    checks (Pylint C0103) while preserving the script behavior.
    """

    # Input text to be encrypted
    text = "Hello Talha"

    # Number of positions to shift each letter
    shift = 3

    # Define the alphabet for encryption
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Store the encrypted result
    encrypted_text: str = ""

    # Iterate through each character in the input text
    for char in text.lower():
        # Preserve spaces in the encrypted text
        if char == " ":
            encrypted_text += char
        else:
            # Find position of current character in alphabet
            index: int = alphabet.find(char)
            # Calculate new position after shift (wrap around using modulo)
            new_index: int = (index + shift) % len(alphabet)
            # Add encrypted character to result
            encrypted_text += alphabet[new_index]

    print("encrypted text:", encrypted_text)

    return encrypted_text


if __name__ == "__main__":
    main()
