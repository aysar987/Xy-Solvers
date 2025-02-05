import base64

encoded_string = "b2pqKSl+ZmpmdG5vamZyY25jYmRoY2JuaW5rZmBuKjlOSUJRTEpVVkBONV9QNTRXSUlXUEhJQ0lIRjVAM101MEpONUAzXV1TSFVXX1RJRTBPMzBTMVc0Mg=="
decoded_bytes = base64.b64decode(encoded_string)
print(f"Decoded bytes: {decoded_bytes}")
for key in range(256):
    decrypted_bytes = bytes([b ^ key for b in decoded_bytes])
    print(f"Attempting key {key}: {decrypted_bytes[:30]}...")
    
    try:
        decrypted_text = decrypted_bytes.decode('utf-8')
        print(f"Decrypted text: {decrypted_text[:150]}...")  
        if decrypted_text.startswith("CIU2025{") and decrypted_text.endswith("}"):
            print(f"Found flag: {decrypted_text}")
            break
    except UnicodeDecodeError:
        continue
