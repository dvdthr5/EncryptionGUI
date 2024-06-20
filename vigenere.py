alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

def generate_keystream(plaintext, keyword):
    keystream = []
    keyword_length = len(keyword)
    keyword_upper = keyword.upper()
    keyword_lower = keyword.lower()
    
    for i, char in enumerate(plaintext):
        if char.isupper():
            keystream.append(keyword_upper[i % keyword_length])
        elif char.islower():
            keystream.append(keyword_lower[i % keyword_length])
        else:
            keystream.append(char)
    
    return ''.join(keystream)

def vigEncode(plaintext, keyword):
    keystream = generate_keystream(plaintext, keyword)
    ciphertext = []
    
    for p_char, k_char in zip(plaintext, keystream):
        if p_char in alphabet_upper:
            shift = alphabet_upper.index(k_char.upper())
            i = alphabet_upper.index(p_char)
            letter = alphabet_upper[(i + shift) % len(alphabet_upper)]
        elif p_char in alphabet_lower:
            shift = alphabet_lower.index(k_char.lower())
            i = alphabet_lower.index(p_char)
            letter = alphabet_lower[(i + shift) % len(alphabet_lower)]
        else:
            letter = p_char  # Non-alphabet characters are unchanged
        ciphertext.append(letter)
    
    return ''.join(ciphertext)

def vigDecode(ciphertext, keyword):
    keystream = generate_keystream(ciphertext, keyword)
    plaintext = []
    
    for c_char, k_char in zip(ciphertext, keystream):
        if c_char in alphabet_upper:
            shift = alphabet_upper.index(k_char.upper())
            i = alphabet_upper.index(c_char)
            letter = alphabet_upper[(i - shift) % len(alphabet_upper)]
        elif c_char in alphabet_lower:
            shift = alphabet_lower.index(k_char.lower())
            i = alphabet_lower.index(c_char)
            letter = alphabet_lower[(i - shift) % len(alphabet_lower)]
        else:
            letter = c_char  # Non-alphabet characters are unchanged
        plaintext.append(letter)
    
    return ''.join(plaintext)

# Example usage
if __name__ == "__main__":
    plaintext = "Hello, World!"
    keyword = "KEY"
    ciphertext = vigEncodencode(plaintext, keyword)
    print(f"Encoded: {ciphertext}")
    decoded_text = vigDecodeecode(ciphertext, keyword)
    print(f"Decoded: {decoded_text}")