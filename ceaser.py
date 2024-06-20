alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

def cipEncode(plaintext, shift=3):
    ciphertext = []
    for char in plaintext:
        if char in alphabet_upper:
            i = alphabet_upper.index(char)
            letter = alphabet_upper[(i + shift) % len(alphabet_upper)]
        elif char in alphabet_lower:
            i = alphabet_lower.index(char)
            letter = alphabet_lower[(i + shift) % len(alphabet_lower)]
        else:
            letter = char  # Non-alphabet characters are unchanged
        ciphertext.append(letter)
    return ''.join(ciphertext)

def cipDecode(ciphertext, shift=-3):
    plaintext = []
    for char in ciphertext:
        if char in alphabet_upper:
            i = alphabet_upper.index(char)
            letter = alphabet_upper[(i + shift) % len(alphabet_upper)]
        elif char in alphabet_lower:
            i = alphabet_lower.index(char)
            letter = alphabet_lower[(i + shift) % len(alphabet_lower)]
        else:
            letter = char  # Non-alphabet characters are unchanged
        plaintext.append(letter)
    return ''.join(plaintext)