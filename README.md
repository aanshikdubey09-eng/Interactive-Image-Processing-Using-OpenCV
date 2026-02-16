<h1 align="center">Interactive Image Processing Using OpenCV</h1>

This project is a menu-driven image processing tool built using Python and OpenCV.  
It allows users to apply multiple classical computer vision operations on an input image through an interactive console interface.

The main objective of this project was to understand how core image processing techniques work at the pixel level and how they can be combined into a simple processing pipeline.

---

## Features

- Convert image to Grayscale
- Apply Gaussian and Median Blur
- Canny Edge Detection
- Binary and Inverse Thresholding
- Contour Detection with object counting
- HSV-based Color Detection
- Image Resizing
- Save Processed Image
- Option to apply multiple operations sequentially

Each operation can be selected from a simple menu after providing the image path.

---

## Technologies Used

- Python
- OpenCV
- NumPy

---

## How to Run

1. Clone this repository:
git clone https://github.com/your-username/interactive-image-processing-opencv.git


2. Install dependencies:
pip install -r requirements.txt


3. Run the program:
python main.py


4. Enter the image filename when prompted (make sure the image is in the same folder or provide full path).

---

## Project Structure

interactive-image-processing-opencv/
│
├── main.py
├── README.md
├── requirements.txt
├── sample_images/
└── screenshots/


---

## What I Learned

While working on this project, I focused on understanding:

- How images are represented as matrices
- How filtering reduces noise
- How Canny detects edges using gradients
- How contours represent object boundaries
- How HSV color space helps in color segmentation

This project strengthened my fundamentals in classical computer vision before moving towards advanced techniques.

---

## Future Improvements

- Add a graphical user interface (GUI)
- Extend support to video processing
- Integrate feature detection algorithms
- Add real-time webcam support

---

This project is created for learning and portfolio purposes.