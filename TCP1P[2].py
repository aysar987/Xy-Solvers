from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from sympy import mod_inverse

# Given values
n = 108968789941102923575789782324105157048081583298436404233965777037328275395317447971475170222848170276248363720650211191108917184545108194739700861856535002088548988035805537888053797268684664758612721011514012937464195321586643070395256055917268428154404753024032378570647091443869315108151218791577942089217
invp = 7407291125786135381861433253169371480648843772183363165710942438089125700005320653922706631492560245328549554249050934552008453971401732902171951518473109
invq = 3212083205272723147020980709364704405125727104023370781697451020238629472626925494104933395667410442713964562283771868303355788208668239546450045357418477
ct = b'\x95\x1c\xfc\x9e\x81\xe6\\l\x0b4\x1a\x0e\xba\x95\xb1\x9d\xb9\xb1\xa9\xc9\x91\x98\xdb\xa8\xa6;\xb8P\x12\xcb\xf9\x1e\xf0\xab\x84\x9f \xe4\x90\x10\xb5+6Hy \xc0\x99\xdf\xea\x83\x80\xe5\xf8\x97\xbdJ2\x8a\xd0\x97\xb4\xba\xb4\x13\xcb\x93\x86E\xbe\xceK\xea3\xedL5\'\x86\xef\x92\x1d\xc4\x07m3\x00|\x02\xden\xe9\xd8om\xb2\x08\xda2"=\xa0\xbaj\x9e5=\x8f\x9cv\xa2\xb5T\xb6\xc0\xe80\xa8\x11\xbc\x95R\x0c\xf7\xd6Ai\x9d'

# Step 1: Compute p and q using the modular inverses invp and invq
# We can use invp and invq to find p and q

# Find p and q
# p = mod_inverse(invp, n) and q = mod_inverse(invq, n)

# Extracting the values
p = mod_inverse(invp, n)
q = mod_inverse(invq, n)


# Step 2: Calculate the private exponent d
# To compute d, we need to use the formula for d: d = mod_inverse(e, (p-1)*(q-1)), where e is the public exponent (usually 65537)
e = 65537
phi_n = (p - 1) * (q - 1)
d = mod_inverse(e, phi_n)

# Step 3: Create the RSA key with the private exponent and decrypt the ciphertext
private_key = RSA.construct((n, e, d, p, q))

# Step 4: Decrypt the ciphertext using PKCS1_OAEP
cipher = PKCS1_OAEP.new(private_key)
plaintext = cipher.decrypt(ct)

# Print the decrypted plaintext
print("Decrypted message:", plaintext.decode())
