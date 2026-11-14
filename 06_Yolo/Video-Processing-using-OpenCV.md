# Day 7 – Video Processing using OpenCV

**Date:** 14 November 2026  
**Topic:** Video Processing and Frame Extraction using OpenCV

## 1. Introduction to Video Processing

Video processing is the process of capturing, reading, analysing and manipulating video data using computer-based techniques.

In Computer Vision, videos are processed as a sequence of individual images called **frames**.

### Key concepts
- A video consists of multiple frames displayed sequentially.
- Each frame is an individual image.
- Frames are processed using image-processing techniques.
- OpenCV provides tools to read, display and manipulate video streams.

### Applications
- CCTV surveillance
- Object tracking
- Human activity recognition
- Autonomous vehicles
- Fall detection
- Traffic monitoring

## 2. Understanding Video Frames

A **frame** is a single image extracted from a video.

A video appears continuous because multiple frames are displayed rapidly one after another.

### Important concepts

| Concept | Description |
|---|---|
| Frame | A single image in a video |
| FPS | Frames Per Second |
| Resolution | Width and height of a video frame |
| Frame extraction | Obtaining individual images from a video |
| Video stream | A continuous sequence of video frames |

### Frames Per Second (FPS)

FPS represents the number of frames displayed or processed per second.

For example:
- 15 FPS means 15 frames per second.
- 30 FPS means 30 frames per second.
- 60 FPS means 60 frames per second.

Higher FPS generally produces smoother motion.

## 3. Introduction to OpenCV Video Processing

OpenCV provides the `VideoCapture` class to access video files and camera streams.

### Important functions

| Function | Purpose |
|---|---|
| `cv2.VideoCapture()` | Opens a video file or camera |
| `cap.read()` | Reads the next video frame |
| `cv2.imshow()` | Displays a video frame |
| `cv2.waitKey()` | Controls frame display timing and keyboard input |
| `cap.release()` | Releases the video capture resource |
| `cv2.destroyAllWindows()` | Closes OpenCV display windows |

## 4. Reading Video Frames

The `VideoCapture()` function is used to open a video.

Example:

```python
import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Understanding the code

1. Open the video using `cv2.VideoCapture()`.
2. Check whether the video is opened successfully.
3. Read frames using `cap.read()`.
4. Check whether a frame was successfully retrieved.
5. Display the frame using `cv2.imshow()`.
6. Use `cv2.waitKey()` to control playback and check for a key press.
7. Release the video resource after processing.

### Understanding `ret` and `frame`

- `ret`: Boolean value indicating whether the frame was read successfully.
- `frame`: The actual image data retrieved from the video.

If `ret` is `False`, the frame could not be read, often because the video has ended.

## 5. Video Properties

OpenCV allows us to retrieve important information about a video.

Examples of video properties include:
- Frame width
- Frame height
- Frames per second
- Total number of frames

Example:

```python
import cv2

cap = cv2.VideoCapture("video.mp4")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

print("Width:", width)
print("Height:", height)
print("FPS:", fps)
print("Total Frames:", frame_count)

cap.release()
```

## 6. Frame-by-Frame Processing

One of the important concepts in video processing is analysing individual frames separately.

Since every video is made up of frames, image-processing operations can also be applied to video frames.

Examples:
- Converting frames to grayscale.
- Applying image thresholding.
- Detecting edges.
- Detecting objects.
- Tracking movement.

### Video Processing Workflow

1. Capture the video.
2. Read individual frames.
3. Apply image-processing operations.
4. Analyse the processed frames.
5. Display or save the output.

## 7. Python Practical

**Platform:** Python / Jupyter Notebook

**Library:** OpenCV (`cv2`)

### Practical concepts

- Opening a video using OpenCV.
- Reading video frames.
- Understanding frame extraction.
- Displaying frames.
- Understanding video properties.
- Releasing video resources properly.

### Important distinction

Image processing works on individual images, whereas video processing involves processing a sequence of frames over time.

## 8. Day 7 Learning Outcomes

By completing this lesson, I learned:

- Fundamentals of video processing.
- Understanding videos as sequences of frames.
- Introduction to FPS and video resolution.
- Reading videos using `cv2.VideoCapture()`.
- Extracting frames using `cap.read()`.
- Displaying video frames using OpenCV.
- Understanding important video properties.
- Frame-by-frame processing workflow.

## 9. Assessment Results

| Lesson | Topic | Score |
|---|---|---:|
| Lesson 3 | Video Processing using OpenCV | 5/5 |
| **Total** | | **5/5** |

**Overall quiz performance: 100%**
