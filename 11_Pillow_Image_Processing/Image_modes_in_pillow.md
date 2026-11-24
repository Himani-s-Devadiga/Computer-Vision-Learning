-----------------
 Image Modes
-----------------

Pillow supports several image modes that describe how pixel data is represented.
Mode	Description
RGB	Red, Green, and Blue channels.
RGBA	Red, Green, Blue, and Alpha channels.
L	Grayscale image.
1	1-bit black-and-white image.

The Alpha channel controls transparency. An Alpha value of 255 represents a fully opaque pixel, while a value of 0 represents a fully transparent pixel.
5. Image Conversion
Convert an image to grayscale:
gray = image.convert("L")gray.save("outputs/grayscale.png")

Convert an RGBA image to RGB:
rgb_image = image.convert("RGB")rgb_image.save("outputs/rgb.png")

6. Image Resizing
The resize() method changes an image to the specified dimensions.
resized = image.resize((800, 400))

The thumbnail() method resizes an image so that it fits within the specified dimensions while maintaining its aspect ratio.
resized = image.copy()resized.thumbnail((800, 800))resized.save("outputs/resized.png")

7. Image Cropping
Cropping extracts a specific rectangular region from an image.
cropped = image.crop((0, 0, 1059, 230))cropped.save("outputs/cropped.png")

The crop coordinates are specified in this order:

(left, upper, right, lower)
8. Image Rotation
rotated = image.rotate(90, expand=True)rotated.save("outputs/rotated.png")

The expand=True parameter expands the output image dimensions, when necessary, to accommodate the rotated image without cropping its corners.
9. Image Flipping
Horizontal flip:
flipped = ImageOps.mirror(image)flipped.save("outputs/flipped.png")

Vertical flip:
vertical_flip = ImageOps.flip(image)vertical_flip.save("outputs/vertical_flip.png")

10. Accessing Pixel Values
pixel = image.getpixel((100, 100))print("Pixel value:", pixel)

Practical output:
Pixel value: (178, 182, 193, 255)

Because the original image is in RGBA mode, this tuple represents the Red, Green, Blue, and Alpha values of the pixel at coordinate (100, 100).
Practical Implementation
Created pillow_basics.py to perform the following operations:
- Image loading and inspection.
- Grayscale conversion.
- RGB conversion.
- Image resizing.
- Image cropping.
- Image rotation.
- Horizontal and vertical flipping.
- Pixel-value inspection.
Key Learning: Pillow provides a straightforward interface for image manipulation and is useful for preparing images before computer vision and OCR tasks.
