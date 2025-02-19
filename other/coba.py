def decrypt_flag(encrypted_hex, key):
    
    key_length = len(key)
    
    for i, byte in enumerate(encrypted_bytes):
        val = byte ^ ord(key[i % key_length])
        
        val -= carry
        if val < 0:
            val += 256
        
        flag.append(chr(val))
        
        carry += val
        carry %= 256
    return ''.join(flag)
encrypted_hex = "23a326c27bee9b40885df97007aa4dbe410e93"
key = "Awesome!"

decrypted_flag = decrypt_flag(encrypted_hex, key)
print(decrypted_flag)