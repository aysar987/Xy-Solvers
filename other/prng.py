c_hex = "25a71013140a54bdccaaeee9a4dae19d734a58cf04919bb0"
c_bytes = bytes.fromhex(c_hex)

prefix = "bronco{"
p_bytes = [ord(c) for c in prefix]
prng = [c_bytes[i] ^ p_bytes[i] for i in range(len(prefix))]

for coefficient in range(256):
    constant_term = (prng[1] - coefficient * prng[0]) % 256
    if all((coefficient * prng[i] + constant_term) % 256 == prng[i+1] for i in range(len(prng) - 1)):
        extended_prng_sequence = prng.copy()
        for _ in range(len(c_bytes) - len(prefix)):
            next_value = (coefficient * extended_prng_sequence[-1] + constant_term) % 256
            extended_prng_sequence.append(next_value)

        decrypted_bytes = bytes([cb ^ prng for cb, prng in zip(c_bytes, extended_prng_sequence)])
        try:
            decrypted_flag = decrypted_bytes.decode('ascii')
            if decrypted_flag.startswith('bronco{') and '}' in decrypted_flag:
                print(f"Flag: {decrypted_flag}")
                break
        except UnicodeDecodeError:
            continue
else:
    print(".")
