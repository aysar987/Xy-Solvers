import hashlib
import secrets

def decryption(encrypted_text, seed):
    decrypted = []
    
    random = secrets.SystemRandom(seed)
    
    for i, char in enumerate(encrypted_text):
        char_code = ord(char)
        shift = (i + 1) * 3
        original = (char_code - shift - 67) % 256
        decrypted.append(chr(original))
    
    return ''.join(decrypted)

with open('VaultKey_encrypted.txt', 'r', encoding='utf-8') as f:
    encrypted_text = f.read()

original_text = ""  
secret_key = str(sum(ord(c) for c in original_text))
secret_key = secret_key[::-1]
hashed_key = hashlib.sha256(secret_key.encode()).hexdigest()
seed = int(hashed_key[:16], 16)

decrypted_text = decryption(encrypted_text, seed)
print(decrypted_text)
