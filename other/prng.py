c_hex = "25a71013140a54bdccaaeee9a4dae19d734a58cf04919bb0" #hex dari output yang diberikan 

c_bytes = bytes.fromhex(c_hex) #mengubah hex menjadi bytes

pref = "bronco{" #prefix bagian flag yang diketahui 

p_bytes = [ord(char) for char in pref] #mengubah prefix yang diketahui menjadi list ASCII

prng = [c_bytes[i] ^ p_bytes[i] for i in range(len(pref))] #Melakukan XOR antara byte dari data dengan byte dari pref, selama loop berjalan

for coefficient in range(256):
    constant_term = (prng[1] - coefficient * prng[0]) % 256 #menentukan nilai konstan dengan menggunakan rumus 
    if all((coefficient * prng[i] + constant_term) % 256 == prng[i+1] for i in range(len(prng) - 1)): #memastikan pola yang dihasilkan oleh koefisien dan konstanta tersebut cocok dengan urutan PRNG
        extended_prng_sequence = prng.copy() 
        for _ in range(len(c_bytes) - len(pref)):
            next_value = (coefficient * extended_prng_sequence[-1] + constant_term) % 256
            extended_prng_sequence.append(next_value) #Apabila berhasil maka akan menyesuaikan PRNG dengan panjang flag yang terenkripsi 

        decrypted_bytes = bytes([cb ^ prng for cb, prng in zip(c_bytes, extended_prng_sequence)]) #melakukan XOR antara sequence PRNG 
        try:
            decrypted_flag = decrypted_bytes.decode('ascii') #mengkonversi bytes menjadi string yang dapat dibaca dengan menggunakan encoding ASCII.
            if decrypted_flag.startswith('bronco{') and '}' in decrypted_flag:
                print(f"Flag: {decrypted_flag}") #syarat untuk memberikan output flag adalah memenuhi syarat
                break
        except UnicodeDecodeError:
            continue
else:
    print(".")
