# Global Thresholding

## 1. Objective
To separate foreground and background regions of an image using a single fixed threshold value.

## 2. Theory
Global Thresholding is a basic image segmentation technique that converts a grayscale image into a binary image using one threshold value for the entire image.

Each pixel's intensity is compared with the selected threshold.

- Pixels greater than the threshold are assigned white (255).
- Pixels less than or equal to the threshold are assigned black (0).

The threshold value determines how foreground and background regions are separated.

## 3. Procedure
1. Load the input image using OpenCV.
2. Convert the image into grayscale.
3. Select a suitable threshold value.
4. Apply thresholding using `cv2.threshold()`.
5. Save and display the resulting binary image.

## 4. OpenCV Function
`cv2.threshold()`

## 5. Observation
The grayscale image is converted into a binary image containing black and white regions. The segmentation result depends on the selected threshold value.
