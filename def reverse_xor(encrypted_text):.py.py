def reverse_xor(encrypted_text):
    reversed_text = []
    for i, c in enumerate(encrypted_text):
        if i % 2 == 0:  # XOR only the even indexed characters
            reversed_text.append(chr(ord(c) ^ 42))
        else:
            reversed_text.append(c)
    return ''.join(reversed_text)

# Example usage
encrypted_text = "P ±»¾u¼ÊÌÆ³ÒØêõî÷¬úð®øüûÀÉ&æÛ&6,ñ@ðLENNÿHQIRVl^ay=&noxI}xX\¥hp¯v¶ÀÎ^"
decrypted_text = reverse_xor(encrypted_text)
print(decrypted_text)
