import cv2
import os
import numpy as np

# List of expected output images
files = [
    "morphology_eroded.png",
    "morphology_dilated.png",
    "morphology_opening.png",
    "morphology_closing.png",
    "morphology_opening_5x5.png"
]

print("MORPHOLOGICAL OPERATIONS VERIFICATION\n")

for filename in files:

    path = os.path.join("outputs", filename)

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print(filename, "NOT FOUND")
        continue

    print("File:", filename)
    print("Dimensions:", image.shape)
    print("Pixel values:", np.unique(image))
    print("File exists and is readable: YES")
    print("-" * 40)

print("Verification completed!")