import cv2
import cv2.aruco as aruco
from fpdf import FPDF
import numpy as np


# def draw_marker(dictionary, marker_id, side_pixels):
#     """
#     Draws an ArUco marker image.
#
#     Args:
#         dictionary: The ArUco dictionary to use.
#         marker_id: The ID of the marker to draw.
#         side_pixels: The size of the marker in pixels (width and height).
#
#     Returns:
#         A NumPy array representing the marker image.
#     """
#
#     marker_bits = dictionary.bytesList[marker_id]
#     marker_image = np.zeros((side_pixels, side_pixels), dtype=np.uint8)
#
#     # Fill in the marker pixels based on the bit pattern
#     for y in range(side_pixels):
#         for x in range(side_pixels):
#             bit_index = y * side_pixels + x
#             byte_index = bit_index // 8  # Get the byte index
#             byte_value = marker_bits[byte_index]  # Extract the byte value
#
#             if (byte_value & (1 << (7 - bit_index % 8))) != 0:
#                 marker_image[y, x] = 255
#
#     return marker_image
#
#
# # Dictionary for ArUco markers
# aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
#
# # Create a PDF object
# pdf = FPDF()
#
# # Loop through marker IDs
# for marker_id in range(1, 51):
#     # Create an ArUco marker
#     marker = draw_marker(aruco_dict, marker_id, 200)
#
#     # Create a new page in the PDF
#     pdf.add_page()
#     pdf.set_font('Arial', size=12)
#     pdf.cell(200, 10, txt=f'ArUco Marker ID: {marker_id}', ln=1, align='C')
#
#     # Convert the marker to RGB and save it as a PNG
#     marker_rgb = cv2.cvtColor(marker, cv2.COLOR_BGR2RGB)
#     cv2.imwrite(f'marker_{marker_id}.png', marker_rgb)
#
#     # Add the marker image to the PDF
#     pdf.image(f'marker_{marker_id}.png', x=10, y=20, w=180, h=180)
#
# # Save the PDF file
# pdf.output('aruco_markers.pdf', 'F')
# print("ArUco markers PDF generated successfully!")

# Define dictionary size and marker size
dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
marker_size = 200

# Generate and save markers
for i in range(5):
    marker_id = i
    marker_image = aruco.drawMarker(dictionary, marker_id, marker_size)
    cv2.imwrite(f"marker_{marker_id}.png", marker_image)

    # Display generated marker
    cv2.imshow(f"Marker {marker_id}", marker_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
