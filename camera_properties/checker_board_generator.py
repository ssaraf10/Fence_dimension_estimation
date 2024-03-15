import cv2
import numpy as np

# Define the dimensions of the checkerboard
rows = 8  # Number of rows of squares
cols = 6  # Number of columns of squares
square_size = 100  # Size of each square in millimeters (mm)

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

# Set the DPI (dots per inch) for printing
dpi = 300  # Adjust as needed

# Calculate the image resolution in pixels per inch (PPI)
ppi = dpi * 25.4  # 1 inch = 25.4 mm

# Calculate the image dimensions in inches
image_width_inches = image_width / ppi
image_height_inches = image_height / ppi

# Save the checkerboard image with the correct size for printing
# cv2.imwrite('checkerboard.png', board, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.imwrite('checkerboard.bmp', board)
print(
    f"Checkerboard image saved as 'checkerboard.png' with dimensions: {image_width} x {image_height} pixels ({image_width_inches:.2f} x {image_height_inches:.2f} inches)")