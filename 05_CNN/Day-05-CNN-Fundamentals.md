# Day 5 – CNN Fundamentals

**Date:** 10 November 2026  
**Topic:** Deep Learning and Convolutional Neural Networks

## 1. Introduction to Deep Learning

Deep Learning is a subset of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from data.

### Key concepts
- Uses multi-layer neural networks.
- Learns complex patterns from data.
- Can automatically extract useful features.
- Widely used in computer vision, speech recognition and natural language processing.

### Applications
- Face recognition
- Medical image analysis
- Handwriting recognition
- Autonomous vehicles
- Object detection

## 2. Introduction to CNN

CNN stands for **Convolutional Neural Network**.

It is a Deep Learning architecture specially designed to process image data and recognize visual patterns.

### Why CNN?
Images are represented as numerical pixel values. CNNs learn useful visual features from these values.

Examples of learned features:
- Edges
- Lines
- Curves
- Textures
- Shapes

### CNN vs Traditional Neural Networks

| Traditional Neural Network | CNN |
|---|---|
| Often flattens image pixels | Preserves spatial image structure |
| Can require many parameters for images | Uses shared filters |
| Does not naturally preserve local spatial relationships after flattening | Learns local visual patterns |
| Used for general prediction tasks | Particularly effective for image processing |

## 3. Convolution, Filters and Kernels

**Convolution** is an operation in which a small matrix called a filter or kernel moves across an image to extract visual features.

### Kernel
A kernel is a small matrix of numerical weights, commonly 3×3 or 5×5.

Example:

```python
import numpy as np

kernel = np.array([
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
])
```

### How convolution works
1. Place the kernel over an image region.
2. Multiply corresponding pixel and kernel values.
3. Add the multiplication results.
4. Store the result.
5. Move the kernel to the next position.

Different kernels can respond to different visual patterns.

In CNNs, filters are generally learned automatically during model training.

## 4. Feature Maps

A **feature map** is the output generated when a filter is applied to an input image through convolution.

### Important points
- Different filters produce different feature maps.
- Early CNN layers often learn edges and lines.
- Middle layers can learn textures and shapes.
- Deeper layers can learn more complex visual patterns.

### Filter vs Feature Map

| Filter / Kernel | Feature Map |
|---|---|
| Small matrix of weights | Output matrix |
| Used to process an image | Represents detected patterns |
| Input to convolution | Output of convolution |

A convolutional layer with 32 filters typically produces 32 feature maps for a single input example.

## 5. Pooling

Pooling reduces the spatial dimensions (height and width) of feature maps while retaining useful information.

### Types of pooling

**Max Pooling**
- Selects the maximum value from each region.
- Preserves strong activations.

**Average Pooling**
- Calculates the average value from each region.
- Summarizes values in a region.

Example of max pooling:

Input:

```text
1  3  2  4
5  6  1  2
7  2  8  3
4  1  2  9
```

Output using 2×2 max pooling with stride 2:

```text
6  4
7  9
```

### Benefits of pooling
- Reduces feature-map dimensions.
- Reduces computational requirements.
- Retains useful information.
- Provides some tolerance to small spatial shifts.

## 6. Image Classification

Image classification is the task of assigning a category or label to an image.

Examples:
- Cat
- Dog
- Car

### Simplified CNN workflow

1. Input image
2. Convolution
3. Feature extraction
4. Pooling
5. Classification layers
6. Predicted output

## 7. Python Practical

**Platform:** Google Colab

**Libraries:** NumPy, OpenCV and Matplotlib

### Tasks completed
- Imported NumPy, OpenCV and Matplotlib.
- Created a 5×5 grayscale image using NumPy.
- Visualized the original image.
- Created a 3×3 vertical-edge detection kernel.
- Applied convolution using `cv2.filter2D()`.
- Generated and visualized a feature map.
- Created a horizontal-edge detection kernel.
- Compared the outputs produced by different kernels.

### Important functions

```python
cv2.filter2D(image, cv2.CV_32F, kernel)
```

Used to apply a filter to an image and generate a convolution output.

```python
plt.imshow(feature_map, cmap="gray")
```

Used to visualize the feature map.

## 8. Day 5 Learning Outcomes

By completing Day 5, I learned:

- Fundamentals of Deep Learning.
- Introduction to Convolutional Neural Networks.
- Convolution, filters and kernels.
- Feature-map generation.
- Max pooling and average pooling.
- Fundamentals of image classification.
- Practical implementation of convolution using Python.

## 9. Assessment Results

| Lesson | Topic | Score |
|---|---|---:|
| Lesson 1 | Introduction to Deep Learning | 4/4 |
| Lesson 2 | Introduction to CNN | 4/4 |
| Lesson 3 | Convolution, Filters and Kernels | 4/4 |
| Lesson 4 | Feature Maps | 4/4 |
| Lesson 5 | Pooling and Image Classification | 4/4 |
| **Total** | | **20/20** |

**Overall quiz performance: 100%**
