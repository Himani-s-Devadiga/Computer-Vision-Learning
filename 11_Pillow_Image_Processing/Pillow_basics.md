# Pillow (PIL) Fundamentals

## Introduction

Pillow is a Python imaging library and the maintained successor to the Python Imaging Library (PIL).

It provides tools for opening, manipulating, processing, and saving images.

## Installation

```bash
pip install Pillow
```

## Importing Pillow

```python
from PIL import Image, ImageOps
```

## Opening and Displaying Images

```python
image = Image.open("sample.png")
image.show()
```

- `Image.open()` opens an image file.
- `image.show()` displays the image.

## Image Properties

```python
print(image.size)
print(image.format)
print(image.mode)
```

Important properties:

- Size: Image width and height in pixels.
- Format: File format such as PNG, JPEG or BMP.
- Mode: Pixel representation and color channels.

## Image Modes

| Mode | Description |
|---|---|
| RGB | Red, Green and Blue channels |
| L | Grayscale image |
| 1 | Black-and-white binary image |
| RGBA | RGB with an Alpha transparency channel |

## Image Mode Conversion

```python
gray_image = image.convert("L")
rgb_image = image.convert("RGB")
```

- `convert("L")` converts an image to grayscale.
- `convert("RGB")` converts an image to RGB mode.

## Resizing Images

```python
resized = image.resize((500, 300))
```

Resizing changes the image dimensions.

To preserve the aspect ratio:

```python
image.thumbnail((800, 800))
```

## Cropping Images

```python
cropped = image.crop((left, upper, right, lower))
```

Cropping extracts a selected region of an image.

## Rotating Images

```python
rotated = image.rotate(90, expand=True)
```

Rotates an image by the specified angle.

## Flipping Images

```python
flipped = ImageOps.mirror(image)
```

Creates a horizontal mirror image.

## Saving Images

```python
image.save("output.png")
```

Saves the processed image to a file.

## Applications in Computer Vision

- Image preprocessing
- Image format conversion
- Image resizing and cropping
- Preparing images for OCR
- Preparing datasets for deep learning

## Pillow vs OpenCV

| Pillow | OpenCV |
|---|---|
| Image manipulation library | Computer vision library |
| Simple image operations | Advanced image processing |
| Uses RGB for common color images | Uses BGR by default |
| Useful for opening, editing and saving images | Useful for filtering, thresholding, detection and analysis |

## Key Takeaway

Pillow provides essential image manipulation operations that are useful in computer vision workflows, particularly when preparing images for OCR and deep learning.

**Progress:** Theory covered. Practical implementation pending.
