# Lesson 3: OpenCV Advanced Image Manipulation

## 1. Introduction to OpenCV

OpenCV (Open Source Computer Vision Library) is a computer vision library used for image processing, video analysis, object detection, and other visual computing tasks.

**Install OpenCV:**

```bash
pip install opencv-python
```

**Import the libraries:**

```python
import cv2
import numpy as np
```

## 2. Reading an Image

The `cv2.imread()` function loads an image.

```python
image = cv2.imread("images/handwritten_sample.png")
```

Check whether the image loaded successfully:

```python
if image is None:
    raise FileNotFoundError("Image not found")
```

## 3. Understanding Image Properties

```python
print("Image shape:", image.shape)
print("Data type:", image.dtype)
```

**Practical output:**

```text
Image shape: (487, 1059, 3)
Data type: uint8
```

**Explanation:**

- `487`: Image height.
- `1059`: Image width.
- `3`: Number of color channels.
- `uint8`: Unsigned 8-bit integer pixel data, generally ranging from 0 to 255.

## 4. Understanding BGR and RGB

OpenCV uses BGR channel ordering by default, whereas Pillow commonly uses RGB.

**Convert BGR to RGB:**

```python
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

**Convert BGR to grayscale:**

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Grayscale conversion produces a single intensity channel.

## 5. Image Resizing

```python
resized = cv2.resize(
    image,
    (800, 400),
    interpolation=cv2.INTER_AREA
)
```

Interpolation determines how pixel values are calculated during resizing.

**Common interpolation methods:**

| Method | Application |
|---|---|
| `INTER_NEAREST` | Nearest-neighbor interpolation |
| `INTER_LINEAR` | Linear interpolation |
| `INTER_CUBIC` | Cubic interpolation |
| `INTER_AREA` | Often useful for image shrinking |

## 6. Image Cropping

OpenCV uses NumPy array slicing for cropping.

```python
cropped = image[0:230, 0:1059]
```

The syntax is:

```python
image[y1:y2, x1:x2]
```

Unlike Pillow, OpenCV uses row and column indexing through NumPy arrays.

## 7. Image Translation

Translation moves an image horizontally or vertically.

```python
height, width = image.shape[:2]

matrix = np.float32([
    [1, 0, 50],
    [0, 1, 30]
])

translated = cv2.warpAffine(
    image,
    matrix,
    (width, height)
)
```

**Here:**

- `50` represents horizontal movement in pixels.
- `30` represents vertical movement in pixels.

## 8. Image Rotation

```python
height, width = image.shape[:2]

center = (width // 2, height // 2)

rotation_matrix = cv2.getRotationMatrix2D(
    center, 45, 1
)

rotated = cv2.warpAffine(
    image,
    rotation_matrix,
    (width, height)
)
```

**Parameters:**

- `center`: Point around which the image rotates.
- `45`: Rotation angle in degrees.
- `1`: Scaling factor.

## 9. Saving Images

The `cv2.imwrite()` function saves processed images.

```python
cv2.imwrite("outputs/opencv_gray.png", gray)
cv2.imwrite("outputs/opencv_resized.png", resized)
cv2.imwrite("outputs/opencv_cropped.png", cropped)
cv2.imwrite("outputs/opencv_translated.png", translated)
cv2.imwrite("outputs/opencv_rotated.png", rotated)
```

## 10. Practical Implementation

Created `opencv_manipulation.py` to perform:

- Image loading and inspection.
- BGR to RGB conversion.
- Grayscale conversion.
- Image resizing.
- Cropping.
- Translation.
- Rotation.
- Saving processed images.

**Practical output:**

```text
Image shape: (487, 1059, 3)
Data type: uint8
OpenCV manipulation completed!
```

## 11. Applications in Computer Vision

OpenCV manipulation techniques are useful for:

- Document preprocessing.
- Image alignment.
- Handwriting orientation correction.
- Image resizing for deep learning models.
- Extracting specific text regions.
- Preparing images for OCR pipelines.

## Key Learning

OpenCV provides powerful image-processing operations and is widely used in computer vision and real-time image applications.
