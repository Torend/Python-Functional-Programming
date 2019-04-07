

# encrypting using a Caesar cipher
def encrypt_caesar_cipher(plaintext):
    return ''.join([caesar_encode(c) for c in plaintext])


# decrypting using a Caesar cipher
def decrypt_caesar_cipher(ciphertext):
    return ''.join([caesar_decode(c) for c in ciphertext])


# encode one character using a Caesar cipher
def caesar_encode(c):
    if 65 <= ord(c) <= 87:
        return chr(ord(c) + 3)
    elif 88 <= ord(c) <= 90:
        return chr(ord(c) % 88 + 65)
    else:
        return c


# decode one character using a Vigenère cipher
def caesar_decode(c):
    if 68 <= ord(c) <= 90:
        return chr(ord(c) - 3)
    elif 65 <= ord(c) <= 67:
        return chr(ord(c) + 23)
    else:
        return c


# encrypting using a Vigenère cipher
def encrypt_vigenere_cipher(plaintext, keyword):
    return ''.join([vigenere_encode(c, key) for c, key in zip(plaintext, key_matching(keyword, len(plaintext)))])


# decrypting using a Vigenère cipher
def decrypt_vigenere_cipher(ciphertext, keyword):
    return ''.join([vigenere_decode(c, key) for c, key in zip(ciphertext, key_matching(keyword, len(ciphertext)))])


# encode one character using a Vigenère cipher
def vigenere_encode(c, key):
    if 65 <= ord(c) <= 90:
        if ord(key) + ord(c) - 65 <= 90:
            return chr(ord(key) + ord(c) - 65)
        else:
            return chr(ord(key) + ord(c) - 91)
    else:
        return c


# decode one character using a Vigenère cipher
def vigenere_decode(c, key):
    if 65 <= ord(c) <= 90:
        if 65 <= ord(c) - ord(key) + 65:
            return chr(ord(c) - ord(key) + 65)
        else:
            return chr(ord(c) - ord(key) + 91)
    else:
        return c


# matching the keyword to fit the length of the plaintext
def key_matching(key, length):
    return [key[i % len(key)] for i in range(length)]


# encrypting using a Morse code
def encrypt_morse_code(plaintext):
    return ''.join([morse_encode(c) for c in plaintext])


# decrypting using a Morse code
def decrypt_morse_code(ciphertext):
    return ''.join([morse_decode(c) for c in ''.join(ciphertext).split()])


# encode one character using a Morse code
# encode space between two words to '/'
def morse_encode(c):
    MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                       'C': '-.-.', 'D': '-..', 'E': '.',
                       'F': '..-.', 'G': '--.', 'H': '....',
                       'I': '..', 'J': '.---', 'K': '-.-',
                       'L': '.-..', 'M': '--', 'N': '-.',
                       'O': '---', 'P': '.--.', 'Q': '--.-',
                       'R': '.-.', 'S': '...', 'T': '-',
                       'U': '..-', 'V': '...-', 'W': '.--',
                       'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2': '..---', '3': '...--',
                       '4': '....-', '5': '.....', '6': '-....',
                       '7': '--...', '8': '---..', '9': '----.',
                       '0': '-----', ' ': '/'}
    if MORSE_CODE_DICT.get(c) is not None:
        return MORSE_CODE_DICT[c]+' '
    else:
        return c + ' '


# decode one character using a Morse code
def morse_decode(c):
    MORSE_DECODE_DICT = {'.-': 'A', '-...': 'B',
                         '-.-.': 'C', '-..'	: 'D', '.': 'E',
                         '..-.': 'F', '--.'	: 'G', '....': 'H',
                         '..'	: 'I', '.---': 'J', '-.-': 'K',
                         '.-..': 'L', '--': 'M', '-.': 'N',
                         '---': 'O', '.--.': 'P', '--.-': 'Q',
                         '.-.': 'R', '...': 'S', '-': 'T',
                         '..-': 'U', '...-': 'V', '.--': 'W',
                         '-..-': 'X', '-.--': 'Y','--..': 'Z',
                         '.----': '1', '..---': '2', '...--': '3',
                         '....-': '4', '.....': '5', '-....': '6',
                         '--...': '7', '---..': '8', '----.': '9',
                         '-----': '0', '/': ' '}
    if MORSE_DECODE_DICT.get(c) is not None:
        return MORSE_DECODE_DICT[c]
    else:
        return c

# if __name__ == "__main__":
#     s = "PYTHON"
#     s2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     s3 = ""
#     print(s2)
#     print(encrypt_caesar_cipher(s2))
#     print(decrypt_caesar_cipher(encrypt_caesar_cipher(s2)))
#     print(key_matching("LEMON", 12))
#     print(encrypt_vigenere_cipher("ATTACKATDAWN","LEMON"))
#     print(decrypt_vigenere_cipher(encrypt_vigenere_cipher("ATTACKATDAWN", "LEMON"), "LEMON"))
#     x = encrypt_morse_code("LA^LA TOR$$N123")
#     print(x)
#     print(decrypt_morse_code(x))
#     print(encrypt_morse_code(s3))