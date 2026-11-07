# Day 4 – Image Preprocessing

## Learning Objectives

Today, I learned how image preprocessing techniques improve image quality and prepare images for further computer vision tasks.

Topics covered:
1. Image Preprocessing Fundamentals
2. Image Thresholding
3. Noise Removal and Filtering
4. Gaussian Blur and Image Sharpening
5. Edge Detection and Contours

---

## 1. Image Preprocessing Fundamentals

Image preprocessing is the process of modifying an image to improve its quality and make it suitable for further analysis.

### Why is preprocessing needed?

Images may contain:
- Noise and unwanted dots
- Uneven lighting
- Low contrast
- Blurred details
- Unclear object boundaries

Preprocessing helps improve image quality before applying computer vision algorithms.

### Common preprocessing operations

- Resizing
- Grayscale conversion
- Noise removal
- Thresholding
- Blurring
- Sharpening
- Edge detection

---

## 2. Image Thresholding

Thresholding is an image processing technique that converts a grayscale image into a binary image based on pixel intensity.

### Types of Thresholding

**1. Binary Thresholding**

Pixels above the threshold become white (255), while pixels at or below it become black (0).

**2. Binary Inverse Thresholding**

The output is the reverse of binary thresholding.

**3. Adaptive Thresholding**

Uses different local thresholds for different regions of an image.

Useful when lighting conditions are uneven.

**4. Otsu's Thresholding**

Automatically calculates a suitable global threshold based on the image's intensity distribution.

### Important OpenCV Functions

- `cv2.threshold()`
- `cv2.adaptiveThreshold()`

### Key Learning

Thresholding helps separate foreground objects, such as handwriting, from the background, such as paper.

---

## 3. Noise Removal and Filtering

### What is Image Noise?

Image noise refers to unwanted random variations in pixel values that affect image quality.

Examples:
- Salt-and-pepper noise
- Grainy patterns
- Random bright or dark pixels

### What is Filtering?

Filtering modifies pixel values using information from neighbouring pixels.

Filtering can be used for smoothing, noise reduction and image enhancement.

### Types of Filters

**1. Average Filter**

- Calculates the average of neighbouring pixel values.
- Smooths the image.
- Can blur edges.

OpenCV: `cv2.blur()`

**2. Gaussian Filter**

- Uses a weighted average of neighbouring pixels.
- Gives more weight to pixels near the centre.
- Helps reduce Gaussian-like noise.

OpenCV: `cv2.GaussianBlur()`

**3. Median Filter**

- Replaces a pixel with the median value of its neighbourhood.
- Particularly effective against salt-and-pepper noise.
- Often preserves edges better than average filtering.

OpenCV: `cv2.medianBlur()`

**4. Bilateral Filter**

- Smooths an image while preserving strong edges.
- Useful when noise reduction is needed without losing important boundaries.
- Can be computationally slower than simpler filters.

OpenCV: `cv2.bilateralFilter()`

### Difference Between Noise Removal, Filtering and Thresholding

| Concept | Meaning |
|---|---|
| Noise Removal | Reduces unwanted noise |
| Filtering | Modifies pixels using neighbouring pixels |
| Thresholding | Separates pixels based on intensity |

**Memory trick: Clean → Smooth → Separate**

---

## 4. Gaussian Blur and Image Sharpening

### Gaussian Blur

Gaussian Blur is a smoothing technique that reduces small details and noise using a weighted average of neighbouring pixels.

OpenCV: `cv2.GaussianBlur()`

Important parameters:
- Input image
- Kernel size
- Sigma value

A larger kernel generally produces stronger smoothing.

### Image Sharpening

Image sharpening enhances edges and fine details, making an image appear clearer.

It can be performed using a sharpening kernel and `cv2.filter2D()`.

### Difference

| Gaussian Blur | Sharpening |
|---|---|
| Smooths the image | Enhances details |
| Reduces small variations | Emphasizes edges |
| Suppresses fine details | Makes details more prominent |

**Remember: Blur = Smooth | Sharpen = Enhance**

---

## 5. Edge Detection and Contours

### Edge Detection

Edge detection identifies boundaries in an image where pixel intensity changes significantly.

Common edge detection techniques:

**1. Canny Edge Detection**

A popular edge detection algorithm that follows five main steps:

1. Noise reduction using Gaussian Blur
2. Gradient calculation
3. Non-Maximum Suppression
4. Double Thresholding
5. Edge Tracking by Hysteresis

OpenCV: `cv2.Canny()`

**2. Sobel Edge Detection**

Detects intensity changes in horizontal and vertical directions.

- Sobel X: Primarily detects vertical edges.
- Sobel Y: Primarily detects horizontal edges.

OpenCV: `cv2.Sobel()`

**3. Laplacian Edge Detection**

Detects rapid intensity changes in multiple directions using second-order derivatives.

OpenCV: `cv2.Laplacian()`

### What are Contours?

Contours are continuous curves that connect boundary points of an object.

They help identify and represent object outlines.

Important OpenCV functions:

- `cv2.findContours()` – Finds contours in a binary image.
- `cv2.drawContours()` – Draws detected contours.

Important contour retrieval modes:

- `cv2.RETR_EXTERNAL` – Retrieves only external contours.
- `cv2.CHAIN_APPROX_SIMPLE` – Compresses contour points by removing redundant points.

### Difference Between Edge Detection and Contours

| Edge Detection | Contours |
|---|---|
| Identifies image boundaries | Groups boundary points into curves |
| Detects intensity changes | Represents object outlines |
| Examples: Canny, Sobel | Example: `findContours()` |

### Edge Detection vs Canny

Edge detection is the overall task of finding boundaries in an image.

Canny is one algorithm used to perform edge detection.

Other methods include Sobel and Laplacian.

---

## 6. Practical Learning

During this lesson, I practised:

- Loading and preprocessing images.
- Converting images to grayscale.
- Applying different thresholding methods.
- Comparing four filtering techniques.
- Applying Gaussian Blur.
- Sharpening images using a custom kernel.
- Detecting edges using Canny and Sobel.
- Finding and drawing contours.

Practical code and output comparisons are maintained separately in the Day 4 notebook.

---

## 7. Application in Computer Vision Projects

| Application | Relevant Concepts |
|---|---|
| Handwritten Prescription Recognition | Grayscale, denoising, thresholding and image enhancement |
| CCTV Object Detection | Image preprocessing, edge analysis and object detection |
| Fall Detection | Video preprocessing, object detection and pose estimation |

**Important:** Not every project requires every preprocessing technique. The appropriate operations depend on image quality, the dataset and the model being used.

---

## 8. Key Takeaways

- Image preprocessing improves image quality before further analysis.
- Thresholding separates foreground and background based on pixel intensity.
- Different filters are useful for different types of noise.
- Gaussian Blur smooths images, while sharpening enhances details.
- Edge detection identifies boundaries in images.
- Canny, Sobel and Laplacian are different edge detection methods.
- Contours represent object outlines.

---

## 9. Day 4 Assessment

| Lesson | Quiz Score |
|---|---:|
| Image Preprocessing Fundamentals | 4/4 |
| Image Thresholding | 4/4 |
| Noise Removal and Filtering | 4/4 |
| Gaussian Blur and Sharpening | 4/4 |
| Edge Detection and Contours | 5/5 |
| **Total** | **21/21** |

**Day 4 Status: Completed**

Next Learning Goal: Continue building practical Computer Vision skills and explore how preprocessing supports OCR, object detection and video analysis.
