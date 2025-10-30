"""
Vigenère Cipher Implementation

This module implements the Vigenère cipher, a method of encrypting alphabetic text
by using a series of interwoven Caesar ciphers based on the letters of a keyword.

The Vigenère cipher is more secure than a simple Caesar cipher because it uses
different shift values for each letter based on a repeating key.

Example:
    plaintext:  "congratulations in success"
    key:        "happycoding"
    ciphertext: "mrttaqrhknsw ih puggrur"
"""

# Sample encrypted text and decryption key
ENCRYPTED_TEXT = "mrttaqrhknsw ih puggrur"
DECRYPTION_KEY = "happycoding"

# Alphabet constant for the cipher
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def vigenere(message: str, key: str, direction: int = 1) -> str:
    """
    Encrypt or decrypt a message using the Vigenère cipher.

    The Vigenère cipher shifts each letter in the message by an amount determined
    by the corresponding letter in the key. The key repeats if it's shorter than
    the message.

    Args:
        message: The text to encrypt or decrypt
        key: The encryption/decryption key (should contain only letters)
        direction: 1 for encryption, -1 for decryption (default: 1)

    Returns:
        The encrypted or decrypted message

    Raises:
        ValueError: If the key is empty or contains non-alphabetic characters
    """
    # Validate the key
    if not key:
        raise ValueError("Key cannot be empty")
    if not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters")

    key = key.lower()
    key_index = 0
    final_message = ""

    for char in message.lower():
        # Preserve non-alphabetic characters (spaces, punctuation, etc.)
        if not char.isalpha():
            final_message += char
        else:
            # Get the current key character (wraps around if message is longer than key)
            key_char = key[key_index % len(key)]
            key_index += 1

            # Calculate the shift amount based on the key character's position
            offset = ALPHABET.index(key_char)

            # Find current character's position in the alphabet
            index = ALPHABET.find(char)

            # Apply the shift (forward for encryption, backward for decryption)
            # Modulo ensures we wrap around the alphabet (z -> a)
            new_index = (index + offset * direction) % len(ALPHABET)

            # Add the shifted character to the result
            final_message += ALPHABET[new_index]

    return final_message


def encrypt(message: str, key: str) -> str:
    """
    Encrypt a message using the Vigenère cipher.

    Args:
        message: The plaintext message to encrypt
        key: The encryption key

    Returns:
        The encrypted ciphertext
    """
    return vigenere(message, key, direction=1)


def decrypt(message: str, key: str) -> str:
    """
    Decrypt a message using the Vigenère cipher.

    Args:
        message: The ciphertext to decrypt
        key: The decryption key (must be the same as the encryption key)

    Returns:
        The decrypted plaintext
    """
    return vigenere(message, key, direction=-1)


def main() -> None:
    """
    Main function demonstrating encryption and decryption.

    Decrypts the sample encrypted text using the provided key and displays
    the original message.
    """
    print("\n" + "=" * 50)
    print("VIGENÈRE CIPHER - DECRYPTION DEMO")
    print("=" * 50)

    print(f"\nEncrypted text: {ENCRYPTED_TEXT}")
    print(f"Decryption key: {DECRYPTION_KEY}")

    try:
        # Decrypt the message
        decrypted_message = decrypt(ENCRYPTED_TEXT, DECRYPTION_KEY)
        print(f"Decrypted text: {decrypted_message}")

        # Demonstrate encryption by re-encrypting the decrypted message
        print("\n" + "-" * 50)
        print("VERIFICATION - RE-ENCRYPTING THE DECRYPTED TEXT")
        print("-" * 50)
        re_encrypted = encrypt(decrypted_message, DECRYPTION_KEY)
        print(f"Re-encrypted:   {re_encrypted}")
        print(f"Original:       {ENCRYPTED_TEXT}")
        print(f"Match: {re_encrypted == ENCRYPTED_TEXT}")

    except ValueError as e:
        print(f"\nError: {e}")

    print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
