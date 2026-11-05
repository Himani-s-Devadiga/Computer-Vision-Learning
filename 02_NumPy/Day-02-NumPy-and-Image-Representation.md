# Day 02 – NumPy and Image Representation

**Date:** November 5, 2026

## Topics Learned

### 1. Computer Vision Fundamentals
- Introduction to Computer Vision.
- Understanding how computers interpret images.
- Applications of Computer Vision.
- Image classification, object detection, segmentation and OCR.

### 2. Understanding Images
- Images are represented as numerical arrays.
- Pixels are the smallest units of an image.
- Pixel values generally range from 0 to 255 for standard 8-bit images.
- Grayscale images are represented using 2D arrays.
- Colour images are represented using 3D arrays.

### 3. NumPy Fundamentals
- Creating arrays using `np.array()`.
- Understanding array dimensions.
- Accessing elements using indexing.
- Understanding image shape and size.

### 4. Image Properties

| Property | Meaning |
|---|---|
| `image.shape` | Image dimensions |
| `image.size` | Total number of elements |
| `image.dtype` | Data type of pixels |

For a colour image, the shape is generally:

`(height, width, channels)`

### 5. OpenCV Concepts
- OpenCV reads colour images in BGR format by default.
- RGB and BGR channel ordering.
- Accessing individual pixels using array indexing.

Example:

```python
import numpy as np

image = np.array([
    [0, 100, 255],
    [50, 150, 200]
])

print(image)
print(image.shape)
print(image.dtype)
```

## Quiz Results

- Computer Vision Fundamentals: 5/5
- NumPy and Image Representation: 5/5

## Key Takeaways

- An image is essentially a numerical array.
- Understanding NumPy is important for image processing.
- Image dimensions and pixel values are fundamental concepts in Computer Vision.

- Practise image processing using Python.

**Status:** Theory and practical exercises completed; 
