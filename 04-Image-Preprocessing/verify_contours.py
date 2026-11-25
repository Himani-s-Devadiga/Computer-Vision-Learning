
import cv2
import os

files = [
    "outputs/contour_binary.png",
    "outputs/detected_contours.png"
]

for file in files:
    image = cv2.imread(file)

    if image is None:
        print("Could not load:", file)
    else:
        print(
            file,
            "| Shape:", image.shape,
            "| Data type:", image.dtype
        )

# Verify binary image
binary = cv2.imread(
    "outputs/contour_binary.png",
    cv2.IMREAD_GRAYSCALE
)

if binary is not None:
    print("Binary pixel values:", sorted(set(binary.flatten())))

print("Contour verification completed!")
