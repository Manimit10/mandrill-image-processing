import struct

# Define the file path
file_path = "4_mandrill-u8be-3x512x512.raw"

# Define image dimensions
width = 512
height = 512

# Define the position you want to read
x = 100
y = 200

# Calculate the byte offset for the specified position
byte_offset = (y * width + x) * 3  # 3 components (R, G, B) per pixel

# Open the binary file in binary read mode
with open(file_path, 'rb') as file:
    # Move to the specified byte offset
    file.seek(byte_offset)

    # Read the RGB values as 8-bit unsigned integers in big-endian format
    red_byte, green_byte, blue_byte = struct.unpack('>BBB', file.read(3))

# Print the RGB values
print(f"Red: {red_byte}, Green: {green_byte}, Blue: {blue_byte}")