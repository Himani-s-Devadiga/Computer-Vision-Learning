# Lesson 5: Sobel and Canny Edge Detection

## 1. Introduction to Edge Detection

Edge detection is an image-processing technique used to identify boundaries where image intensity changes significantly.

It helps identify important structural information in an image.

**Common applications:**

- Identifying character boundaries.
- Detecting object outlines.
- Document analysis.
- Shape detection.
- Image segmentation.
- Preparing images for further computer vision operations.

In handwritten prescription OCR, edge detection can help reveal the structure of handwritten strokes and character boundaries.

## 2. Understanding Image Gradients

An image gradient measures how quickly pixel intensity changes across an image.

There are two main gradient directions:

- **X-gradient:** Measures intensity changes horizontally and highlights mostly vertical edges.
- **Y-gradient:** Measures intensity changes vertically and highlights mostly horizontal edges.

## 3. Sobel Edge Detection

The Sobel operator is an edge-detection technique that calculates image intensity changes in the horizontal and vertical directions.

It uses two kernels (small matrices).

**Sobel X kernel:**

```text
-1   0   1
-2   0   2
-1   0   1
```

Detects mostly vertical edges.

**Sobel Y kernel:**

```text
-1  -2  -1
 0   0   0
 1   2   1
```

Detects mostly horizontal edges.

**Gradient magnitude:**

The gradient magnitude combines both directions:

\[
G = \sqrt{G_x^2 + G_y^2}
\]

A higher gradient magnitude indicates a stronger intensity change and potentially a stronger edge.

### OpenCV Implementation

**Sobel X:**

```python
sobel_x = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)
```

**Sobel Y:**

```python
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)
```

**Parameters:**

- `gray`: Input grayscale image.
- `cv2.CV_64F`: Uses 64-bit floating-point output to preserve positive and negative gradients.
- `1, 0`: Calculates the X-gradient.
- `0, 1`: Calculates the Y-gradient.
- `ksize=3`: Uses a 3 × 3 Sobel kernel.

### Converting Gradient Results

Sobel produces floating-point gradient values. `cv2.convertScaleAbs()` converts them into an 8-bit image suitable for visualization.

```python
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)
```

### Combining Sobel X and Y

```python
sobel_combined = cv2.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)
```

This combines the two gradient images into one visualization.

## 4. Canny Edge Detection

Canny Edge Detection is a multi-stage edge-detection algorithm developed by John F. Canny.

It identifies strong and meaningful edges while reducing unwanted noise.

Unlike basic Sobel detection, Canny uses several processing stages to produce a cleaner edge map.

### Five Steps of Canny Edge Detection

**Step 1: Noise Reduction**

Gaussian Blur is applied to reduce noise before detecting edges.

```python
blurred = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)
```

**Step 2: Gradient Calculation**

The algorithm calculates intensity changes in the horizontal and vertical directions to identify possible edges.

**Step 3: Non-Maximum Suppression**

This step makes detected edges thinner by retaining local maximum gradient values and suppressing other nearby values.

**Step 4: Double Thresholding**

Two thresholds classify detected gradient values:

- Strong edges: Above the high threshold.
- Weak edges: Between the low and high thresholds.
- Non-edges: Below the low threshold.

**Step 5: Edge Tracking by Hysteresis**

Weak edges connected to strong edges are retained. Weak edges not connected to strong edges are removed.

The result is a cleaner edge map.

### OpenCV Implementation

```python
canny = cv2.Canny(
    blurred,
    50,
    150
)
```

**Parameters:**

- `blurred`: Input image after Gaussian smoothing.
- `50`: Lower threshold.
- `150`: Upper threshold.

These are example threshold values. The best values depend on the image.

## 5. Sobel vs Canny

| Feature | Sobel | Canny |
|---|---|---|
| Purpose | Calculates image gradients | Detects edges |
| Noise reduction | Not built into the basic operator | Uses Gaussian smoothing |
| Edge thickness | Can produce thicker edges | Produces thinner edges |
| Processing | Relatively simple | Multi-stage algorithm |
| Output | Gradient information | Binary edge map |

**Key differences:**

- Sobel calculates intensity gradients.
- Canny identifies edges using multiple processing stages.
- Sobel X detects mostly vertical edges.
- Sobel Y detects mostly horizontal edges.

## 6. Practical Implementation

Created `edge_detection.py` to perform Sobel and Canny edge detection.

### Complete Python Program

```python
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

# 1. Sobel X - Vertical edges
sobel_x = cv2.Sobel(
    gray,
    cv2.CV_64F,
    1,
    0,
    ksize=3
)

# 2. Sobel Y - Horizontal edges
sobel_y = cv2.Sobel(
    gray,
    cv2.CV_64F,
    0,
    1,
    ksize=3
)

# Convert gradient results to displayable images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# 3. Combine Sobel X and Y
sobel_combined = cv2.addWeighted(
    sobel_x, 0.5,
    sobel_y, 0.5,
    0
)

# 4. Apply Gaussian Blur
blurred = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

# 5. Canny Edge Detection
canny = cv2.Canny(
    blurred,
    50,
    150
)

# Save results
cv2.imwrite("outputs/sobel_x.png", sobel_x)
cv2.imwrite("outputs/sobel_y.png", sobel_y)
cv2.imwrite("outputs/sobel_combined.png", sobel_combined)
cv2.imwrite("outputs/canny_edges.png", canny)

print("Sobel X, Sobel Y and Canny completed!")
```

### Practical Output

```text
Sobel X, Sobel Y and Canny completed!
```

## 7. Output Verification

Created `verify_edges.py` to verify that all four processed images were saved and could be loaded successfully.

### Verification Program

```python
import cv2

files = [
    "outputs/sobel_x.png",
    "outputs/sobel_y.png",
    "outputs/sobel_combined.png",
    "outputs/canny_edges.png"
]

for file in files:
    image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

    if image is None:
        print("Could not load:", file)
    else:
        print(
            file,
            "| Shape:", image.shape,
            "| Data type:", image.dtype
        )

print("Edge detection verification completed!")
```

### Practical Output

```text
outputs/sobel_x.png | Shape: (487, 1059) | Data type: uint8
outputs/sobel_y.png | Shape: (487, 1059) | Data type: uint8
outputs/sobel_combined.png | Shape: (487, 1059) | Data type: uint8
outputs/canny_edges.png | Shape: (487, 1059) | Data type: uint8
Edge detection verification completed!
```

**Observation:**

All four processed images were successfully generated, saved and loaded.

### Generated Output Files

| File | Description |
|---|---|
| `sobel_x.png` | Mostly vertical edges |
| `sobel_y.png` | Mostly horizontal edges |
| `sobel_combined.png` | Combined gradient information |
| `canny_edges.png` | Thin, detected edges |

All four output images have:

- Dimensions: 487 × 1059 pixels.
- Data type: `uint8`.

## 8. Applications in Handwritten Prescription OCR

Edge detection can be useful when preparing handwritten prescriptions for OCR and handwriting recognition.

**Possible applications:**

- Identifying handwritten character boundaries.
- Studying the structure of character strokes.
- Detecting document and text-region outlines.
- Supporting document segmentation.
- Analysing image quality before OCR processing.

**Important:** Edge detection does not recognize handwritten characters or medicine names. It provides structural information that may support further image-processing operations. Its usefulness should be evaluated on actual prescription images.

## Key Learning

Sobel and Canny are important edge-detection techniques in computer vision.

Sobel calculates horizontal and vertical intensity gradients, while Canny uses a multi-stage algorithm to produce cleaner and thinner edge maps.

These techniques help analyse image structure and can support document processing and OCR pipelines.
