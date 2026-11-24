## Image Modes

Pillow supports different image modes that describe how pixel data is represented.

| Mode | Description |
|---|---|
| RGB | Red, Green, and Blue channels. |
| RGBA | RGB with an additional Alpha channel. |
| L | Grayscale image. |
| 1 | 1-bit black-and-white image. |

The Alpha channel controls transparency.

An Alpha value of 255 represents a fully opaque pixel, while a value of 0 represents a fully transparent pixel.

##  Image Conversion

**Convert an image to grayscale:**

```python
gray = image.convert("L")
gray.save("outputs/grayscale.png")
```

**Convert an RGBA image to RGB:**

```python
rgb_image = image.convert("RGB")
rgb_image.save("outputs/rgb.png")
```

##  Image Resizing

The `resize()` method changes the image dimensions.

```python
resized = image.resize((800, 400))
```

The `thumbnail()` method resizes an image while maintaining its aspect ratio within the specified dimensions.

```python
resized = image.copy()
resized.thumbnail((800, 800))
resized.save("outputs/resized.png")
```

##  Image Cropping

Cropping extracts a specific rectangular region from an image.

```python
cropped = image.crop((0, 0, 1059, 230))
cropped.save("outputs/cropped.png")
```

The coordinates represent:

`(left, upper, right, lower)`

##  Image Rotation

```python
rotated = image.rotate(90, expand=True)
rotated.save("outputs/rotated.png")
```

The `expand=True` parameter adjusts the output dimensions to accommodate the rotated image without cropping its corners.

##  Image Flipping

**Horizontal flip:**

```python
flipped = ImageOps.mirror(image)
flipped.save("outputs/flipped.png")
```

**Vertical flip:**

```python
vertical_flip = ImageOps.flip(image)
vertical_flip.save("outputs/vertical_flip.png")
```

## Accessing Pixel Values

```python
pixel = image.getpixel((100, 100))
print("Pixel value:", pixel)
```

**Practical output:**

```text
Pixel value: (178, 182, 193, 255)
```

This represents the Red, Green, Blue, and Alpha values of the selected pixel.

## Practical Implementation

Created `pillow_basics.py` to perform the following operations:

- Image loading and inspection.
- Grayscale conversion.
- RGB conversion.
- Image resizing.
- Image cropping.
- Image rotation.
- Horizontal and vertical flipping.
- Pixel-value inspection.

**Key Learning:** Pillow provides a simple interface for image manipulation and is useful for preparing images before computer vision and OCR tasks.
