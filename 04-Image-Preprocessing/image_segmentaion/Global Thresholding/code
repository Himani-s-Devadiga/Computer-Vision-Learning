
import cv2

# Load the handwritten image in grayscale
image = cv2.imread(
    r"C:\Users\HIMANI\Intelligent-OCR-Text-Extraction\images\handwritten_sample.png",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    raise FileNotFoundError("Image not found!")

# Apply global thresholding
threshold_value = 127

_, binary_image = cv2.threshold(
    image,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

# Display results
cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Global Thresholding", binary_image)

# Save the output
cv2.imwrite("global_threshold_output.png", binary_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Global thresholding completed successfully!")
