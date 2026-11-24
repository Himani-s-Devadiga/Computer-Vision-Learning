# Lesson 2: Pillow Image Manipulation – Practical

## Objective

To implement common image manipulation operations using Pillow on a handwritten sample image.

## Libraries Used

```python
from PIL import Image, ImageOps
```

## Practical Implementation

```python
from PIL import Image, ImageOps

# Open image
image = Image.open("images/handwritten_sample.png")

# Display image information
print("Image size:", image.size)
print("Image format:", image.format)
print("Image mode:", image.mode)

# Convert to grayscale
gray = image.convert("L")
gray.save("outputs/pillow_grayscale.png")

# Resize while maintaining aspect ratio
resized = image.copy()
resized.thumbnail((800, 800))
resized.save("outputs/pillow_resized.png")

# Crop the first line
cropped = image.crop((0, 0, 1059, 230))
cropped.save("outputs/pillow_cropped.png")

# Rotate image
rotated = image.rotate(90, expand=True)
rotated.save("outputs/pillow_rotated.png")

# Flip horizontally
flipped = ImageOps.mirror(image)
flipped.save("outputs/pillow_flipped.png")

# Convert to RGB
rgb_image = image.convert("RGB")
rgb_image.save("outputs/pillow_rgb.png")

# Access pixel value
print("Pixel value:", image.getpixel((100, 100)))

# Flip vertically
vertical_flip = ImageOps.flip(image)
vertical_flip.save("outputs/pillow_vertical_flip.png")

print("Pillow operations completed!")
```

## Practical Output

```text
Image size: (1059, 487)
Image format: PNG
Image mode: RGBA
Pixel value: (178, 182, 193, 255)
Pillow operations completed!
```

## Important Observations

1. The original image had dimensions of 1059 × 487 pixels.
2. The image was stored in PNG format.
3. Its original mode was RGBA.
4. Grayscale conversion reduced the image to a single intensity channel.
5. Resizing and cropping helped prepare image regions for further processing.
6. Rotation and flipping demonstrated basic geometric transformations.
7. Pixel inspection helped understand how image data is represented.

## Applications in OCR

Pillow can help prepare handwritten documents by:

- Converting images into grayscale.
- Resizing images for model input.
- Cropping individual text lines.
- Correcting image orientation.
- Converting image formats and color modes.

**Key Learning:** Pillow is useful for basic image preparation and manipulation before OCR and handwriting recognition.
