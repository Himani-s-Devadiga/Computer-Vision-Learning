# Lesson 8: Image Segmentation

## 1. What is Image Segmentation?

Image segmentation is the process of dividing an image into meaningful regions or assigning labels to individual pixels.

It helps computers identify and separate important objects or regions within an image.

### Why is Image Segmentation Important?
- Separates foreground from background.
- Identifies objects and regions of interest (ROI).
- Helps improve image recognition.
- Supports OCR and handwriting recognition.
- Useful in medical image analysis and computer vision.

## 2. Types of Image Segmentation

### Semantic Segmentation
Assigns a class label to every pixel in an image. Objects belonging to the same class share the same label.

Example: All pixels representing roads are classified as road.

### Instance Segmentation
Identifies and separates individual objects, even when they belong to the same class.

Example: Separating three individual cars in an image.

### Panoptic Segmentation
Combines semantic and instance segmentation to provide a complete understanding of the image.

## 3. Traditional Image Segmentation Techniques

### A. Threshold-Based Segmentation

Separates pixels based on their intensity values.

**Global Thresholding**
- Uses one fixed threshold value for the entire image.
- Pixels above or below the threshold are assigned different values.
- Works well when lighting is relatively uniform.

**Adaptive Thresholding**
- Calculates different threshold values for local regions.
- Useful for images with uneven illumination.
- OpenCV provides:
  - Adaptive Mean Thresholding
  - Adaptive Gaussian Thresholding

**Otsu's Thresholding**
- Automatically determines a global threshold using the image intensity histogram.
- Reduces within-class intensity variance.
- Useful when foreground and background intensities form reasonably distinct groups.

### B. Edge-Based Segmentation

Uses intensity changes to identify object boundaries.

Common techniques:
- Sobel
- Canny
- Laplacian

### C. Region-Based Segmentation

Groups neighbouring pixels with similar characteristics.

Examples:
- Region Growing
- Region Splitting and Merging

### D. Clustering-Based Segmentation

Groups pixels according to similar features such as colour or intensity.

Example:
- K-Means Clustering

## 4. Practical Implementation Using OpenCV

### Practical 1: Global Thresholding

**File:** `global_thresholding.py`

- Loaded a handwritten image in grayscale.
- Applied a fixed threshold value of 127.
- Used `cv2.threshold()` with `cv2.THRESH_BINARY`.
- Saved the output as `global_threshold_output.png`.

### Practical 2: Adaptive Thresholding

**File:** `adaptive_thresholding.py`

- Used a handwritten photograph with uneven illumination.
- Applied Adaptive Mean Thresholding.
- Applied Adaptive Gaussian Thresholding.
- Used a block size of 21 and C value of 10.
- Compared both methods for handling local lighting variations.

### Practical 3: Otsu's Thresholding

**File:** `otsu_thresholding.py`

- Loaded the handwritten photograph in grayscale.
- Used `cv2.THRESH_BINARY + cv2.THRESH_OTSU`.
- Allowed OpenCV to automatically calculate the threshold.
- Saved the result as `otsu_threshold_output.png`.

## 5. Important OpenCV Functions

| Function | Purpose |
|---|---|
| `cv2.threshold()` | Applies global or Otsu thresholding |
| `cv2.adaptiveThreshold()` | Applies local adaptive thresholding |
| `cv2.THRESH_BINARY` | Produces a binary image |
| `cv2.THRESH_OTSU` | Automatically selects a global threshold |
| `cv2.imshow()` | Displays images |
| `cv2.imwrite()` | Saves processed images |

## 6. Comparison of Thresholding Techniques

| Technique | Threshold Selection | Best Use |
|---|---|---|
| Global | Fixed value | Uniform lighting |
| Adaptive Mean | Local neighbourhood mean | Uneven lighting |
| Adaptive Gaussian | Weighted local neighbourhood | Uneven lighting |
| Otsu | Automatically selected global value | Distinct foreground/background intensity groups |

## 7. Applications of Image Segmentation

- Handwritten Text Recognition (HTR)
- Optical Character Recognition (OCR)
- Medical image analysis
- Object detection and recognition
- Autonomous vehicles
- Industrial inspection
- Background removal

## 8. Key Takeaways

1. Image segmentation divides an image into meaningful regions.
2. Semantic, instance, and panoptic segmentation are its major types.
3. Thresholding is one of the simplest segmentation approaches.
4. Adaptive thresholding is useful for uneven illumination.
5. Otsu's method automatically selects a global threshold.
6. The best segmentation technique depends on image quality and application requirements.

---

**Lesson 8 Status:** Theory completed and OpenCV thresholding practicals implemented. Output verification and visual comparison should be completed before marking the practical fully verified.
