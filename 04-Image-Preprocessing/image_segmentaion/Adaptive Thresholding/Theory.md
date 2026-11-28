# Adaptive Thresholding

## 1. What is Adaptive Thresholding?

Adaptive Thresholding is an image processing technique that converts a grayscale image into a binary image by calculating different threshold values for different regions of the image.

Unlike Global Thresholding, which uses one fixed threshold for the entire image, Adaptive Thresholding calculates thresholds based on the local neighbourhood of each pixel.

## 2. Why is Adaptive Thresholding Needed?

In images with uneven lighting, some regions may be brighter while others are darker.

A single threshold value may not correctly separate the foreground from the background.

Adaptive Thresholding solves this problem by adjusting the threshold locally.

## 3. Types of Adaptive Thresholding

### A. Adaptive Mean Thresholding

- Calculates the average intensity of neighbouring pixels.
- Subtracts a constant value (C) from the calculated mean.
- Uses the resulting value as the local threshold.

### B. Adaptive Gaussian Thresholding

- Calculates a weighted average of neighbouring pixels.
- Nearby pixels receive greater importance than distant pixels.
- Subtracts a constant value (C) from the weighted average.

## 4. Important Parameters in OpenCV

`cv2.adaptiveThreshold()` uses the following parameters:

| Parameter | Description |
|---|---|
| `maxValue` | Maximum value assigned to thresholded pixels (255). |
| `adaptiveMethod` | Mean or Gaussian thresholding method. |
| `thresholdType` | Determines binary or inverse binary output. |
| `blockSize` | Size of the local neighbourhood; must be an odd number greater than 1. |
| `C` | Constant subtracted from the calculated local threshold. |

## 5. Practical Implementation

For this practical:

- Input: Handwritten image with uneven lighting.
- Image mode: Grayscale.
- Adaptive methods: Mean and Gaussian.
- Block size: 21.
- Constant (C): 10.
- Output: Two binary images.

## 6. Applications

- Handwritten text preprocessing.
- Document image processing.
- OCR systems.
- Image analysis under uneven illumination.

## 7. Conclusion

Adaptive Thresholding improves foreground and background separation in images with varying illumination. Adaptive Mean and Adaptive Gaussian methods calculate local thresholds differently, making them useful for document preprocessing and OCR applications.
