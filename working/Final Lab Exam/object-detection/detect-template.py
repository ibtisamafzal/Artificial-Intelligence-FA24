import cv2
import numpy as np
import os

# File paths
source_path = "images/source.jpg"
template_path = "images/template.jpg"
output_path = "output/result.jpg"

# Load source and template images
source_image = cv2.imread(source_path, cv2.IMREAD_COLOR)
template_image = cv2.imread(template_path, cv2.IMREAD_COLOR)

if source_image is None or template_image is None:
    raise FileNotFoundError("One or both of the images were not found. Check the file paths.")

# Template matching
method = cv2.TM_CCOEFF_NORMED
result = cv2.matchTemplate(source_image, template_image, method)

# Threshold for detecting matches
threshold = 0.8  # Adjust as necessary
locations = np.where(result >= threshold)

# Get template dimensions
template_height, template_width = template_image.shape[:2]

# Draw bounding boxes on the source image
for pt in zip(*locations[::-1]):  # Switch columns and rows
    top_left = pt
    bottom_right = (pt[0] + template_width, pt[1] + template_height)
    cv2.rectangle(source_image, top_left, bottom_right, (0, 255, 0), 2)

# Save and display the result
os.makedirs("output", exist_ok=True)
cv2.imwrite(output_path, source_image)
cv2.imshow("Detected Regions", source_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
