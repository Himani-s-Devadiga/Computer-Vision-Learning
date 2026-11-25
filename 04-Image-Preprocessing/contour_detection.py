
import cv2
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Read image in grayscale
gray = cv2.imread(
    "images/handwritten_sample.png",
    cv2.IMREAD_GRAYSCALE
)

if gray is None:
    raise FileNotFoundError("Image not found")

# Convert handwriting into white foreground
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY_INV
)

# Detect external contours
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Draw detected contours
output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

cv2.drawContours(
    output,
    contours,
    -1,
    (0, 255, 0),
    2
)

# Calculate contour measurements
print("Number of contours:", len(contours))

for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)

    print(f"Contour {i + 1}:")
    print("Area:", area)
    print("Perimeter:", perimeter)

# Save outputs
cv2.imwrite("outputs/contour_binary.png", binary)
cv2.imwrite("outputs/detected_contours.png", output)

print("Contour detection completed!")
