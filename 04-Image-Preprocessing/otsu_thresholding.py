
import cv2

image = cv2.imread(
    r"C:\Users\HIMANI\Intelligent-OCR-Text-Extraction\images\real_uneven_lighting_handwriting.png",
    cv2.IMREAD_GRAYSCALE
)

if image is None:
    raise FileNotFoundError("Handwritten image not found!")

# Apply Otsu's thresholding
threshold_value, otsu_image = cv2.threshold(
    image, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Automatically selected threshold:", threshold_value)

cv2.imshow("Original Grayscale Image", image)
cv2.imshow("Otsu Thresholding", otsu_image)

cv2.imwrite("otsu_threshold_output.png", otsu_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Otsu thresholding completed successfully!")
