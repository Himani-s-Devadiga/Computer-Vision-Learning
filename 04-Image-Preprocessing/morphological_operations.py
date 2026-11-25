import cv2
import numpy as np
import os

# Create output folder if it does not exist
os.makedirs("outputs", exist_ok=True)

# Step 1: Load handwritten image in grayscale
image = cv2.imread(
    "images/handwritten_sample.png",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    raise FileNotFoundError("Handwritten sample image not found!")

print("Image loaded successfully!")
print("Image dimensions:", image.shape)

# Step 2: Convert image into binary format
_, binary = cv2.threshold(
    image,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

print("Binary pixel values:", np.unique(binary))

# Step 3: Create a 3x3 rectangular kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3, 3)
)

# Step 4: Apply erosion
eroded = cv2.erode(
    binary,
    kernel,
    iterations=1
)

cv2.imwrite("outputs/morphology_eroded.png", eroded)
print("Erosion completed!")

# Step 5: Apply dilation
dilated = cv2.dilate(
    binary,
    kernel,
    iterations=1
)

cv2.imwrite("outputs/morphology_dilated.png", dilated)
print("Dilation completed!")

# Step 6: Apply morphological opening
opening = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel
)

cv2.imwrite("outputs/morphology_opening.png", opening)
print("Opening completed!")

# Step 7: Apply morphological closing
closing = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel
)

cv2.imwrite("outputs/morphology_closing.png", closing)
print("Closing completed!")

# Step 8: Compare using a larger 5x5 kernel
large_kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (5, 5)
)

opening_5x5 = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    large_kernel
)

cv2.imwrite(
    "outputs/morphology_opening_5x5.png",
    opening_5x5
)

print("5x5 kernel comparison completed!")

print("\nAll morphological operations completed successfully!")
