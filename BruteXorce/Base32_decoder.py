import base64

def decode_base32(encoded_str):
    try:
        decoded_bytes = base64.b32decode(encoded_str)
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str
    except Exception as e:
        return f"Error decoding base32: {e}"

if __name__ == "__main__":
    encoded_input = input("Enter Base32 encoded string: ")
    decoded_output = decode_base32(encoded_input)
    print("Decoded string:", decoded_output)