# Lesson 4: Image Filters, Blurring and Sharpening

## 1. Introduction to Image Filters

Image filters are operations used to modify pixel values to improve image quality or extract useful information.

They are commonly used to:

- Reduce image noise.
- Smooth unwanted variations.
- Preserve important edges.
- Enhance image details.
- Improve image quality before OCR.

Two important filtering objectives are:

**Blurring:** Smooths an image and reduces noise.

**Sharpening:** Enhances edges and makes details more distinct.

## 2. Gaussian Blur

Gaussian Blur smooths an image using a Gaussian-weighted neighborhood.

It is commonly used to reduce small variations and Gaussian-like noise.

**Implementation:**

```python
gaussian = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)
```

**Parameters:**

- `gray`: Input grayscale image.
- `(5, 5)`: Kernel size.
- `0`: Automatically calculated Gaussian standard deviation.

The kernel size must use positive odd dimensions.

**Application:** Reducing small variations before edge detection and image processing.

## 3. Median Blur

Median Blur replaces each pixel with the median value of its surrounding neighborhood.

**Implementation:**

```python
median = cv2.medianBlur(gray, 5)
```

The kernel size determines the neighborhood used for calculating the median.

**Advantages:**

- Particularly effective for salt-and-pepper noise.
- Removes isolated black and white dots.
- Can preserve edges better than ordinary averaging filters in some situations.

**Application:** Cleaning scanned documents containing isolated black or white noise.

## 4. Bilateral Filtering

Bilateral filtering smooths an image while attempting to preserve important edges.

**Implementation:**

```python
bilateral = cv2.bilateralFilter(
    gray,
    9,
    75,
    75
)
```

**Parameters:**

- `9`: Diameter of the pixel neighborhood.
- `75`: Sigma value for color or intensity similarity.
- `75`: Sigma value for spatial distance.

**Advantages:**

- Reduces noise.
- Preserves edges better than many ordinary smoothing filters.
- Can be useful when processing handwritten characters.

**Limitation:** It is generally more computationally expensive than Gaussian Blur.

## 5. Image Sharpening

Sharpening enhances edges and fine image details.

One simple technique is to subtract a blurred version of the image from the original image.

**Implementation:**

```python
blur = cv2.GaussianBlur(
    gray,
    (5, 5),
    0
)

sharpened = cv2.addWeighted(
    gray,
    1.5,
    blur,
    -0.5,
    0
)
```

**Explanation:**

- `gray`: Original image.
- `1.5`: Weight of the original image.
- `blur`: Blurred image.
- `-0.5`: Weight of the blurred image.
- `0`: Additional brightness offset.

This technique is related to unsharp masking.

**Advantages:**

- Enhances edges.
- Makes some details more distinct.
- Can improve the appearance of faint image details.

**Limitation:** Excessive sharpening can amplify noise and create unwanted artifacts.

## 6. Comparing Image Filters

| Filter | Main Purpose | Best-Suited Situation |
|---|---|---|
| Gaussian Blur | Smooths noise | Gaussian-like noise |
| Median Blur | Removes isolated noise | Salt-and-pepper noise |
| Bilateral Filter | Smooths while preserving edges | Edge-sensitive denoising |
| Sharpening | Enhances details | Improving edge visibility |

## 7. Practical Implementation

Created `image_filters.py` to apply all four filters.

**Implementation:**

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

# 1. Gaussian Blur
gaussian = cv2.GaussianBlur(
    gray, (5, 5), 0
)

# 2. Median Blur
median = cv2.medianBlur(gray, 5)

# 3. Bilateral Filter
bilateral = cv2.bilateralFilter(
    gray, 9, 75, 75
)

# 4. Sharpening
blur = cv2.GaussianBlur(
    gray, (5, 5), 0
)

sharpened = cv2.addWeighted(
    gray, 1.5, blur, -0.5, 0
)

# Save results
cv2.imwrite(
    "outputs/gaussian_blur.png",
    gaussian
)

cv2.imwrite(
    "outputs/median_blur.png",
    median
)

cv2.imwrite(
    "outputs/bilateral_filter.png",
    bilateral
)

cv2.imwrite(
    "outputs/sharpened.png",
    sharpened
)

print("All four image filters applied successfully!")
```

## 8. Filter Output Verification

Created `compare_filters.py` to verify that all four processed images could be loaded.

**Implementation:**

```python
import cv2

files = [
    "outputs/gaussian_blur.png",
    "outputs/median_blur.png",
    "outputs/bilateral_filter.png",
    "outputs/sharpened.png"
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

print("Filter comparison completed!")
```

**Practical output:**

```text
outputs/gaussian_blur.png | Shape: (487, 1059, 3) | Data type: uint8
outputs/median_blur.png | Shape: (487, 1059, 3) | Data type: uint8
outputs/bilateral_filter.png | Shape: (487, 1059, 3) | Data type: uint8
outputs/sharpened.png | Shape: (487, 1059, 3) | Data type: uint8
Filter comparison completed!
```

**Observation:** All four processed images were successfully saved and loaded.

**Note:** `cv2.imread()` loads images in color mode by default, so the grayscale PNG files were read back as three-channel BGR images during verification. To load them as grayscale, use:

```python
cv2.imread(file, cv2.IMREAD_GRAYSCALE)
```

## 9. Applications in Handwritten Prescription OCR

Image filtering is important when preparing handwritten prescriptions for OCR and handwriting recognition.

**Possible applications:**

- Gaussian Blur can reduce small image variations.
- Median Blur can remove isolated black and white dots.
- Bilateral Filtering can reduce noise while retaining character boundaries.
- Sharpening can enhance some faint details.

The best filter depends on the image quality and noise characteristics. Applying every filter does not necessarily improve OCR accuracy. The processed results should be compared with the original image and evaluated using OCR metrics such as Character Error Rate (CER) and Word Error Rate (WER).

## Key Learning

Image filters help improve image quality and prepare handwritten documents for subsequent computer vision and OCR processing.

---

# Phase 2 – Progress Summary

| Lesson | Topic | Status |
|---|---|---|
| 1 | Pillow Fundamentals | Theory completed |
| 2 | Pillow Image Manipulation | Practical completed |
| 3 | OpenCV Advanced Image Manipulation | Practical completed |
| 4 | Image Filters, Blurring and Sharpening | Practical completed |

## Skills Acquired

- Pillow image loading and manipulation.
- Understanding RGB, RGBA, grayscale and pixel values.
- Image resizing, cropping, rotation and flipping.
- OpenCV image reading and saving.
- BGR and RGB color-space conversion.
- NumPy image-array slicing.
- Image translation and rotation.
- Gaussian Blur, Median Blur and Bilateral Filtering.
- Image sharpening and filter comparison.
- Preparing images for OCR preprocessing.

## Tools and Libraries

- Python
- Pillow
- OpenCV
- NumPy
