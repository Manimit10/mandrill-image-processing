import struct

# Define the file path
file_path = "4_mandrill-u8be-3x512x512.raw"

# Define image dimensions
width = 512
height = 512

# Initialize a counter for the total number of set bits
total_set_bits = 0

# Open the binary file in binary read mode
with open(file_path, 'rb') as file:
    # Read the entire file
    data = file.read()

    # Iterate through each byte in the data
    for byte in data:
        # Count the set bits in the byte
        set_bits = bin(byte).count('1')
        # Add the count of set bits in this byte to the total count
        total_set_bits += set_bits

# Print the total number of set bits in the image
print("Total number of bits set to 1 in the image:", total_set_bits)
