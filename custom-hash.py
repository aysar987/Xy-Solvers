def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % 2**24
    return str(sum).encode().hex()

while True:
    # Get input from the user
    input_string = input("Enter a string to hash: ")

    # Call the my_hash function and print the result
    hashed_value = my_hash(input_string)
    print(f"The hash of '{input_string}' is: {hashed_value}")

    # Ask the user if they want to hash another string
    repeat = input("Do you want to hash another string? (yes/no): ").lower()
    if repeat != 'y':
        break
