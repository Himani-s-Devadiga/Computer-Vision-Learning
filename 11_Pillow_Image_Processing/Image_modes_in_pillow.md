. Image Modes

Mode

Description

RGB

Red, Green and Blue channels

RGBA

RGB with an additional Alpha channel

L

Grayscale image

1

Black and white image

The Alpha channel controls transparency.

An Alpha value of 255 represents fully opaque pixels, while 0 represents fully transparent pixels.

5. Image Conversion

Convert an image into grayscale:

gray = image.convert("L")
gray.save("outputs/grayscale.png")

Convert RGBA into RGB:

rgb_image = image.convert("RGB")
rgb_image.save("outputs/rgb.png")

6. Image Resizing

The resize() method changes the image dimensions.

resized = image.resize((800, 400))

The thumbnail() method resizes an image while maintaining its aspect ratio within the specified dimensions.

resized = image.copy()
resized.thumbnail((800, 800))
resized.save("outputs/resized.png")

7. Image Cropping

Cropping extracts a specific region from an image.

cropped = image.crop((0, 0, 1059, 230))
cropped.save("outputs/cropped.png")

The coordinates represent:

(left, upper, right, lower)

8. Image Rotation

rotated = image.rotate(90, expand=True)
rotated.save("outputs/rotated.png")

The expand=True parameter adjusts the output dimensions to accommodate the rotated image.

9. Image Flipping

Horizontal flip:

flipped = ImageOps.mirror(image)
flipped.save("outputs/flipped.png")

Vertical flip:

vertical_flip = ImageOps.flip(image)
vertical_flip.save("outputs/vertical_flip.png")

10. Accessing Pixel Values

pixel = image.getpixel((100, 100))
print("Pixel value:", pixel)

Practical output:

Pixel value: (178, 182, 193, 255)

This represents the Red, Green, Blue and Alpha values of the selected pixel.

Practical Implementation

Created pillow_basics.py to perform:

Image loading and inspection

Grayscale conversion

RGB conversion

Resizing

Cropping

Rotation

Horizontal and vertical flipping

Pixel value inspection

Key Learning: Pillow provides a simple interface for image manipulation and is useful for preparing images before computer vision and OCR tasks.
