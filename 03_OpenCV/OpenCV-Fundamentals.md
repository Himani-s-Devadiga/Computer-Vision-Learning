# Day 3 — OpenCV Fundamentals

**Date:** November 6, 2026  
**Learning Track:** Computer Vision  
**Status:** Completed

## Learning Objectives

Today's goal was to understand the fundamentals of OpenCV and learn how to perform basic image operations using Python.

### Topics Covered

1. Introduction to OpenCV
2. Reading and displaying images
3. Image manipulation
4. Colour spaces and grayscale conversion

---

## 1. Introduction to OpenCV

OpenCV stands for **Open Source Computer Vision Library**.

It is a popular computer vision library used for image processing, video analysis, object detection and other computer vision applications.

### Libraries Used

- **OpenCV (`cv2`):** Image processing and computer vision operations.
- **NumPy:** Working with images as multidimensional arrays.
- **Matplotlib:** Displaying and visualising images.

### Checking Library Versions

```python
import cv2
import numpy as np

print("OpenCV Version:", cv2.__version__)
print("NumPy Version:", np.__version__)
```

### Key Concepts

- OpenCV provides tools for image processing and computer vision.
- NumPy represents images as multidimensional arrays.
- Each pixel contains numerical intensity or colour values.

---

## 2. Reading and Displaying Images

### Reading an Image

The `cv2.imread()` function loads an image into Python.

```python
image = cv2.imread("image.jpg")

if image is not None:
    print("Image loaded successfully!")
    print("Image shape:", image.shape)
else:
    print("Unable to load image.")
```

### Image Reading Modes

| Mode | Description |
|---|---|
| `cv2.IMREAD_COLOR` | Loads a colour image |
| `cv2.IMREAD_GRAYSCALE` | Loads an image in grayscale |
| `cv2.IMREAD_UNCHANGED` | Loads the image with its original channels, including alpha when present |

### Displaying Images in Google Colab

OpenCV reads colour images in BGR format, whereas Matplotlib expects RGB.

Therefore, colour conversion is required before displaying an OpenCV image using Matplotlib.

```python
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis("off")
plt.show()
```

### Saving an Image

The `cv2.imwrite()` function saves an image to the specified path.

```python
success = cv2.imwrite("output.jpg", image)

print("Image saved:", success)
```

It returns:
- `True` if the image is saved successfully.
- `False` if the image could not be saved.

---

## 3. Image Manipulation

Image manipulation involves modifying an image's dimensions, orientation or selected region.

### A. Resizing an Image

The `cv2.resize()` function changes the dimensions of an image.

```python
resized = cv2.resize(image, (300, 300))
```

**Important:** The function accepts dimensions in `(width, height)` order.

Common interpolation methods:

- `cv2.INTER_LINEAR`
- `cv2.INTER_AREA`
- `cv2.INTER_CUBIC`

`INTER_AREA` is generally useful when shrinking images.

### B. Cropping an Image

Cropping selects a specific region of an image using NumPy slicing.

```python
cropped = image[50:250, 100:300]
```

**Important:** NumPy slicing follows this order:

`image[y1:y2, x1:x2]`

Rows come first, followed by columns.

### C. Rotating an Image

The `cv2.rotate()` function rotates an image.

```python
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
```

Available rotation options:

- `cv2.ROTATE_90_CLOCKWISE`
- `cv2.ROTATE_90_COUNTERCLOCKWISE`
- `cv2.ROTATE_180`

### D. Flipping an Image

The `cv2.flip()` function flips an image in different directions.

```python
horizontal_flip = cv2.flip(image, 1)
vertical_flip = cv2.flip(image, 0)
both_flip = cv2.flip(image, -1)
```

| Flip Value | Operation |
|---|---|
| `1` | Horizontal flip |
| `0` | Vertical flip |
| `-1` | Both horizontal and vertical |

---

## 4. Colour Spaces and Grayscale Conversion

### A. RGB vs BGR

A colour image generally contains three channels:

- Red
- Green
- Blue

OpenCV uses **BGR** channel order by default, while Matplotlib uses **RGB**.

Conversion:

```python
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

### B. Grayscale Conversion

A grayscale image represents pixels using intensity values rather than three separate colour channels.

For an 8-bit grayscale image:

- `0` represents black.
- `255` represents white.
- Values between 0 and 255 represent different shades of grey.

Conversion:

```python
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Displaying a grayscale image:

```python
plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()
```

### Understanding Image Dimensions

```python
print("Original image:", image.shape)
print("Grayscale image:", gray_image.shape)
```

A colour image generally has three dimensions:

`(height, width, 3)`

A grayscale image has two dimensions:

`(height, width)`

**Application:** Grayscale conversion is useful in handwritten text recognition because it simplifies image representation while preserving important handwriting patterns.

### C. HSV Colour Space

HSV stands for:

- **Hue:** Represents the colour.
- **Saturation:** Represents colour intensity or purity.
- **Value:** Represents brightness.

Conversion:

```python
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

print("HSV image shape:", hsv_image.shape)
```

HSV is useful in colour-based object detection and segmentation because it separates colour information from brightness.

---

## 5. Key Learnings

By completing today's lessons, I learned:

- What OpenCV is and how it works with NumPy.
- How to read, display and save images.
- How OpenCV and Matplotlib differ in colour channel ordering.
- How to resize, crop, rotate and flip images.
- How to convert images into RGB, grayscale and HSV colour spaces.
- How image dimensions change during different operations.
- How to perform basic image operations using Google Colab.

---

## 6. Knowledge Assessment

| Lesson | Score |
|---|---:|
| Introduction to OpenCV | 4/4 |
| Reading and Displaying Images | 5/5 |
| Image Manipulation | 5/5 |
| Colour Spaces and Grayscale | 4/4 |
| **Total** | **18/18 (100%)** |

**Practical Coding:** Completed  
**Code Notebook:** Uploaded separately in this repository  
**Overall Status:** Day 3 successfully completed.

---

## 7. Next Learning Goal

### Day 4 — Image Preprocessing

Planned topics:

- Image thresholding
- Noise removal
- Gaussian blur
- Image sharpening
- Edge detection
- Contour detection

These techniques will help build the foundation for handwritten prescription recognition and other computer vision applications.
