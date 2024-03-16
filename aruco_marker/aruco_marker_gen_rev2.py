import cv2
import numpy as np
import matplotlib.pyplot as plt


# Parameters for A4 paper size (in pixels)
A4_WIDTH_PX = 2480
A4_HEIGHT_PX = 3508

# Parameters for ArUco markers and layout
MARKER_SIZE = 400
MARKERS_PER_ROW = 5
MARKERS_PER_COL = 5
MARGIN = 100  # Margin around the edges of the paper

# Calculate the total size of the grid of markers
grid_width = MARKERS_PER_ROW * MARKER_SIZE
grid_height = MARKERS_PER_COL * MARKER_SIZE

# Calculate the spacing between markers
spacing_x = (A4_WIDTH_PX - 2 * MARGIN - grid_width) // (MARKERS_PER_ROW - 1)
spacing_y = (A4_HEIGHT_PX - 2 * MARGIN - grid_height) // (MARKERS_PER_COL - 1)

# Create a blank white image (A4 size)
paper = np.ones((A4_HEIGHT_PX, A4_WIDTH_PX, 3), dtype=np.uint8) * 255

# Generate ArUco markers
aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters = cv2.aruco.DetectorParameters_create()

for i in range(MARKERS_PER_ROW):
    for j in range(MARKERS_PER_COL):
        marker_id = i * MARKERS_PER_COL + j
        marker_image_gray = cv2.aruco.drawMarker(aruco_dict, marker_id, MARKER_SIZE)
        marker_image_color = cv2.merge([marker_image_gray] * 3)
        x = MARGIN + i * (MARKER_SIZE + spacing_x)
        y = MARGIN + j * (MARKER_SIZE + spacing_y)
        paper[y:y+MARKER_SIZE, x:x+MARKER_SIZE] = marker_image_color

# Save the paper with markers as a BMP file
cv2.imwrite("markers_grid.png", paper)

# Display the paper with markers
plt.imshow(cv2.cvtColor(paper, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
