# Contours and Contour Detection

## 1. Introduction to Contours

A contour is a curve joining continuous points along the boundary of an object or shape.

Contours help identify the boundaries and shapes of objects in an image.

### Applications of Contour Detection

- Object detection
- Shape identification
- Document boundary detection
- Text-region analysis
- Object measurement
- Image segmentation

In handwritten prescription recognition, contours can help identify connected ink regions and approximate text boundaries.

**Important:** One contour does not necessarily represent one character. Connected or overlapping handwriting strokes may form a single contour.

## 2. Contour Detection Pipeline

The general contour detection process involves:

1. Read the image.
2. Convert the image into grayscale.
3. Apply thresholding to create a binary image.
4. Detect contours.
5. Draw the detected contours.

## 3. Binary Thresholding

Contour detection generally works with binary images.

A binary image contains two pixel values:

- 0 – Black
- 255 – White

For dark handwriting on a light background, inverse thresholding is useful because it converts the handwriting into white foreground regions and the paper into a black background.

### OpenCV Implementation

```python
_, binary = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY_INV
)
```

## 4. Finding Contours

OpenCV provides the `cv2.findContours()` function to detect contours in a binary image.

### Syntax

```python
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

**Parameters:**

- `binary`: Input binary image.
- `cv2.RETR_EXTERNAL`: Retrieves only external contours.
- `cv2.CHAIN_APPROX_SIMPLE`: Removes redundant points along straight contour segments.

**Return values:**

- `contours`: List of detected contours.
- `hierarchy`: Describes relationships between contours, such as parent and child contours.

## 5. Contour Retrieval Modes

OpenCV provides different contour retrieval modes.

| Retrieval Mode | Description |
|---|---|
| `cv2.RETR_EXTERNAL` | Retrieves only outermost contours. |
| `cv2.RETR_LIST` | Retrieves all contours without establishing hierarchy. |
| `cv2.RETR_TREE` | Retrieves all contours with complete parent-child hierarchy. |
| `cv2.RETR_CCOMP` | Organizes contours into a two-level hierarchy. |

## 6. Contour Approximation Methods

Contour approximation determines how contour boundary points are stored.

### CHAIN_APPROX_NONE

Stores all points along the contour boundary.

### CHAIN_APPROX_SIMPLE

Removes redundant points along straight lines and stores only important points.

It reduces memory usage compared with storing every boundary point.

## 7. Drawing Contours

The `cv2.drawContours()` function draws detected contours on an image.

### Syntax

```python
cv2.drawContours(
    output,
    contours,
    -1,
    (0, 255, 0),
    2
)
```

**Parameters:**

- `output`: Image on which contours are drawn.
- `contours`: Detected contour list.
- `-1`: Draws all contours.
- `(0, 255, 0)`: Green colour in BGR format.
- `2`: Contour thickness in pixels.

## 8. Contour Area

The `cv2.contourArea()` function calculates the area enclosed by a contour.

```python
area = cv2.contourArea(contours[0])
```

Contour area is measured in square pixels.

## 9. Contour Perimeter

The `cv2.arcLength()` function calculates the length of a contour boundary.

```python
perimeter = cv2.arcLength(
    contours[0],
    True
)
```

The `True` parameter indicates that the contour is closed.

## 10. Applications in Handwriting Recognition

Contour detection can support handwriting recognition by:

- Identifying ink regions.
- Locating approximate text boundaries.
- Analysing connected handwriting components.
- Supporting document image analysis.
- Helping with image segmentation and preprocessing.

However, contour detection alone cannot recognize handwritten words or medicine names. It is a supporting image-processing technique.

## 11. Key Takeaways

- A contour represents the boundary of an object or shape.
- Binary thresholding prepares an image for contour detection.
- `cv2.findContours()` detects contours.
- Retrieval modes control which contours are retrieved.
- Approximation methods control how contour points are stored.
- `cv2.drawContours()` visualizes detected boundaries.
- `cv2.contourArea()` calculates contour area.
- `cv2.arcLength()` calculates contour perimeter.

**Lesson Outcome:** Understand how to detect, draw, analyse and measure contours using OpenCV.
