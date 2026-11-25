
import cv2

# Load handwritten image in grayscale
image = cv2.imread(
    r"C:\Users\HIMANI\Intelligent-OCR-Text-Extraction\images\real_uneven_lighting_handwriting.png",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    raise FileNotFoundError("Handwritten image not found!")

# Adaptive Mean Thresholding
adaptive_mean = cv2.adaptiveThreshold(
    image,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    21,
    10
)

# Adaptive Gaussian Thresholding
adaptive_gaussian = cv2.adaptiveThreshold(
    image,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    21,
    10
)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Adaptive Mean Thresholding", adaptive_mean)
cv2.imshow("Adaptive Gaussian Thresholding", adaptive_gaussian)

# Save outputs
cv2.imwrite("adaptive_mean_output.png", adaptive_mean)
cv2.imwrite("adaptive_gaussian_output.png", adaptive_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Adaptive thresholding completed successfully!")
