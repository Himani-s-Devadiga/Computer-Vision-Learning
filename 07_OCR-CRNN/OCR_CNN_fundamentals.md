
# Computer Vision Learning 

## 1. Image Processing for OCR

Image preprocessing improves image quality before text detection and recognition.

### Techniques Covered

- **Grayscale conversion:** Removes unnecessary colour information while retaining brightness and text patterns.
- **Resizing:** Changes image dimensions to improve OCR processing.
- **Thresholding:** Converts grayscale images into binary images.
- **Otsu Thresholding:** Automatically determines a suitable threshold value.
- **Adaptive Thresholding:** Calculates different threshold values for different image regions.
- **Noise Removal:** Removes unwanted pixels using filters such as Median Blur.
- **Sharpening:** Enhances text edges.
- **Deskewing:** Corrects tilted or rotated text.
- **Morphological Operations:** Includes erosion, dilation, opening and closing.

### Why Grayscale?

Grayscale converts a three-channel colour image into a single-channel image.

It reduces unnecessary colour information and simplifies preprocessing when colour is not important for recognition.

OpenCV uses the following weighted formula:

`Gray = 0.114B + 0.587G + 0.299R`

---

## 2. OCR Pipeline

OCR stands for Optical Character Recognition.

It converts text present in images into machine-readable text.

### Main OCR Pipeline

1. Image Acquisition
2. Image Preprocessing
3. Text Detection
4. Text Recognition
5. Postprocessing
6. Text Extraction and Output

### Text Detection vs Text Recognition

| Text Detection | Text Recognition |
|---|---|
| Identifies where text is located | Identifies what the text says |
| Finds text regions | Converts text regions into characters and words |
| Produces bounding boxes | Produces recognised text |

Example:

Image: A handwritten prescription.

- Detection identifies the region containing the medicine name.
- Recognition attempts to read the medicine name.

---

## 3. Text Detection Algorithms

### EAST

EAST stands for Efficient and Accurate Scene Text Detector.

- Detects text regions in images.
- Predicts text-region geometry.
- Produces bounding boxes or rotated text regions.
- Useful for detecting text in natural scenes.

### CRAFT

CRAFT stands for Character Region Awareness for Text Detection.

- Detects individual character regions.
- Predicts character regions and affinities between characters.
- Groups characters into text regions.
- Useful for irregularly shaped and curved text.

**Important:** EAST and CRAFT are text detection algorithms, not text recognition algorithms.

---

## 4. Bounding Boxes

A bounding box identifies the location of an object or text region in an image.

It is commonly represented using four coordinates:

`(x_min, y_min, x_max, y_max)`

These coordinates represent:

- x_min: Left boundary
- y_min: Top boundary
- x_max: Right boundary
- y_max: Bottom boundary

Bounding boxes help OCR systems identify exactly where text is located.

Note: OpenCV generally uses a top-left coordinate origin. Tesseract's character box output uses a bottom-left origin.

---

## 5. Tesseract OCR

Tesseract is an open-source OCR engine used to extract text from images.

### Tesseract OCR Pipeline

1. Input image
2. Preprocessing
3. Page segmentation
4. Text recognition
5. Output extraction

### OCR Engine Mode (OEM)

OEM determines which OCR engine is used.

- OEM 0 – Legacy engine only
- OEM 1 – LSTM neural network engine only
- OEM 2 – Legacy + LSTM
- OEM 3 – Default based on available engines

### Page Segmentation Mode (PSM)

PSM determines how Tesseract analyses the layout of an image.

| PSM | Description |
|---|---|
| 3 | Fully automatic page segmentation |
| 6 | Assume a uniform block of text |
| 7 | Treat image as a single text line |
| 8 | Treat image as a single word |
| 10 | Treat image as a single character |
| 11 | Sparse text |

### Important Tesseract Extraction Methods

**1. image_to_string()**

Extracts recognised text from an image.

**2. image_to_data()**

Extracts:
- Recognised words
- Confidence scores
- Bounding box coordinates
- Layout information

**3. image_to_boxes()**

Extracts character-level bounding boxes.

### OCR Evaluation Metrics

**Character Error Rate (CER)**

Measures errors at the character level.

`CER = (Substitutions + Deletions + Insertions) / Total Reference Characters`

**Word Error Rate (WER)**

Measures errors at the word level.

`WER = (Substitutions + Deletions + Insertions) / Total Reference Words`

Python library used: `jiwer`.

### Practical Completed

Created a Python program that:
- Reads an image using OpenCV.
- Converts it into grayscale.
- Resizes the image.
- Applies Otsu thresholding.
- Runs Tesseract OCR.
- Extracts recognised text.
- Displays word-level confidence scores.
- Extracts character bounding boxes.
- Evaluates OCR using CER and WER.

Observed results:
- Character Error Rate: approximately 3.80%
- Word Error Rate: approximately 33.33%

---

## 6. CRNN Architecture

CRNN stands for Convolutional Recurrent Neural Network.

It combines CNN and RNN components to recognise text sequences.

### CRNN Architecture

`Input Image → CNN → BiLSTM → CTC → Recognised Text`

### Components

**1. CNN – Convolutional Neural Network**

- Extracts visual features from text images.
- Identifies edges, curves, strokes and character shapes.
- Produces feature maps.

**2. RNN – Recurrent Neural Network**

- Processes sequential information.
- Understands the order of features.
- Maintains information from previous time steps.

**3. BiLSTM – Bidirectional Long Short-Term Memory**

- Processes sequences in both forward and backward directions.
- Uses context from both sides to improve recognition.

**4. CTC – Connectionist Temporal Classification**

- Helps align image features with text sequences.
- Handles cases where input and output sequence lengths differ.
- Uses blank tokens and repeated-character collapsing during decoding.

### Applications

- Handwritten text recognition
- Printed text recognition
- Document digitisation
- Prescription recognition

---

## 7. CNN Feature Extraction for Text Recognition

Feature extraction means identifying useful patterns from an image.

CNNs learn visual patterns such as:
- Edges
- Lines
- Curves
- Corners
- Character strokes
- Character shapes

### Important CNN Operations

**Convolution**

**ReLU Activation**

**Pooling**

### Feature Maps

Feature maps are outputs produced by convolution operations.

They represent visual patterns learned by the CNN and are passed to the recurrent layers in a CRNN.

### CNN vs CRNN

| CNN | CRNN |
|---|---|
| Extracts spatial features | Extracts features and models sequences |
| Learns visual patterns | Learns visual patterns and character order |
| Does not inherently model sequence dependencies | Uses recurrent layers for sequence dependencies |
| Useful for image classification | Useful for text recognition |

### Spatial vs Sequential Patterns

**Spatial patterns:** How visual features are arranged in an image.

Example: The two diagonal strokes and horizontal bar of the letter A.

**Sequential patterns:** The order in which features or characters appear.

Example: Recognising the sequence of letters in the word COMPUTER.

---

## 8. Python Practical – CNN Input Preparation

Created `cnn_text_features.py` using OpenCV and NumPy.

### Operations Performed

1. Read an image using OpenCV.
2. Convert BGR image into grayscale.
3. Resize the image to 128 × 32.
4. Normalize pixel values.
5. Convert the image into a NumPy array.
6. Display the processed image and inspect its shape.

### Normalization

Pixel values are generally represented between 0 and 255.

Normalization converts them into a range between 0 and 1.

`Normalized Pixel = Pixel Value / 255.0`

This helps maintain a consistent input scale for neural network training.

### Practical Output

- Original image shape: `(300, 900)`
- Resized image shape: `(32, 128)`
- Feature input shape: `(32, 128)`
- Data type: `float32`

**Note:** This practical prepares an image for CNN input. It does not yet generate learned CNN feature maps. Actual CNN feature extraction will be implemented using a deep learning framework.

---

## 9. Key Learnings

- Understood the OCR pipeline and its stages.
- Learned the difference between text detection and text recognition.
- Studied EAST and CRAFT text detection algorithms.
- Understood bounding boxes and coordinate systems.
- Learned Tesseract OCR configuration and extraction methods.
- Practised OCR evaluation using CER and WER.
- Understood CRNN architecture.
- Learned the role of CNN, RNN, BiLSTM and CTC.
- Understood spatial and sequential patterns.
- Prepared an image for CNN input using OpenCV and NumPy.

## 10. Next Topics

- RNN Fundamentals
- Feedforward Neural Networks vs RNN
- Sequential data and time steps
- Hidden states and memory
- LSTM Architecture
- CTC Loss and Decoding

---

**Learning Date:** 17 November 2026  
**Domain:** Computer Vision, OCR and Deep Learning  
**Tools:** Python, OpenCV, NumPy, Pillow, Tesseract OCR, pytesseract, jiwer
