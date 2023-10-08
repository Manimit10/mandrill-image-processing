import struct

# Define the input file path
input_file_path = "4_mandrill-u8be-3x512x512.raw"

# Define the output file path
output_file_path = "mandrill_t93_u8be-3x512x512.raw"

# Define image dimensions
width = 512
height = 512

# Open the input binary file in binary read mode
with open(input_file_path, 'rb') as input_file:
    # Read the entire content of the input file
    image_data = input_file.read()

# Create a new bytearray to store the modified image data
modified_image_data = bytearray()

# Iterate through the image data, modifying the green component
for i in range(0, len(image_data), 3):
    # Extract the RGB values as 8-bit unsigned integers in big-endian format
    red_byte, green_byte, blue_byte = struct.unpack('>BBB', image_data[i:i+3])

    # Set the most significant bit of the green component to 1
    green_byte |= 0x80  # Set the MSB to 1 (10000000 in binary)

    # Append the modified RGB values to the new image data
    modified_image_data.extend(struct.pack('>BBB', red_byte, green_byte, blue_byte))

# Write the modified image data to the output file
with open(output_file_path, 'wb') as output_file:
    output_file.write(modified_image_data)

print("Image with MSBs of green component set to 1 saved as 'mandrill_t93_u8be-3x512x512.raw'.")
