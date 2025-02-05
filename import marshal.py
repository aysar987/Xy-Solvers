import marshal
import dis

# Open and read the file
with open("/Users/aysarakbar/Desktop/CTF/Crypto/ular", 'rb') as f:
    s = f.read()

# Unmarshal the code object
marshal_code = marshal.loads(s)

# Disassemble and print the bytecode
dis.dis(marshal_code)
