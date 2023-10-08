import struct

# Define the input file path
input_file_path = "4_mandrill-u8be-3x512x512.raw"

# Define the output file path
output_file_path = "mandrill_t95_s16be-3x512x512.raw"

# Define image dimensions
width = 512
height = 512

# Open the input binary file in binary read mode
with open(input_file_path, 'rb') as input_file:
    # Read the entire content of the input file
    image_data = input_file.read()

# Create a new bytearray to store the modified image data
modified_image_data = bytearray()

# Iterate through the image data, converting from 8-bit unsigned to 16-bit signed
for i in range(0, len(image_data), 3):
    # Extract the RGB values as 8-bit unsigned integers in big-endian format
    red_byte, green_byte, blue_byte = struct.unpack('>BBB', image_data[i:i+3])

    # Convert 8-bit unsigned to 16-bit signed integers
    red_16bit = struct.unpack(">h", bytes([0, red_byte]))[0]
    green_16bit = struct.unpack(">h", bytes([0, green_byte]))[0]
    blue_16bit = struct.unpack(">h", bytes([0, blue_byte]))[0]

    # Append the modified RGB values as 16-bit signed integers to the new image data
    modified_image_data.extend(struct.pack('>hhh', red_16bit, green_16bit, blue_16bit))

# Write the modified image data to the output file
with open(output_file_path, 'wb') as output_file:
    output_file.write(modified_image_data)

print("Image saved as 'mandrill_t95_s16be-3x512x512.raw'.")
