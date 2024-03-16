import cv2
import numpy as np

# Define square size and DPI
square_size = 250  # Size of each square in pixels
dpi = 300  # Dots per inch for printing

# Calculate A4 dimensions in pixels
a4_width_inches = 210 / 25.4
a4_height_inches = 297 / 25.4
a4_width_pixels = int(a4_width_inches * dpi)
a4_height_pixels = int(a4_height_inches * dpi)

# Calculate maximum number of squares that can fit in A4
cols = int(a4_width_pixels / square_size)
rows = int(a4_height_pixels / square_size)

# Calculate the dimensions of the checkerboard image in pixels
image_width = cols * square_size  # Width in pixels
image_height = rows * square_size  # Height in pixels

# Create a black image
board = np.zeros((image_height, image_width, 3), np.uint8)

# Draw the checkerboard pattern
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            # Draw a white square
            board[i * square_size:(i + 1) * square_size, j * square_size:(j + 1) * square_size] = [255, 255, 255]


# Save the checkerboard image with the correct size for printing
# cv2.imwrite('checkerboard.png', board, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.imwrite('checkerboard.png', board)
# print(
#     f"Checkerboard image saved as 'checkerboard.png' with dimensions: {image_width} x {image_height} pixels ({image_width_inches:.2f} x {image_height_inches:.2f} inches)")