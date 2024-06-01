# Face Detection Project

This project is a simple face detection and recognition application built using Python, OpenCV, and the Face Recognition library.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Introduction
The Face Detection Project is a computer vision application that can detect and recognize faces in real-time video from a webcam. It uses the Face Recognition library to encode the faces and compare them to a known face, which should be in the `img/` folder.

## Features
- Real-time face detection and recognition
- Draws bounding boxes around detected faces
- Displays the name of the recognized person (or "Unknown" if not recognized)

## Installation
To run the Face Detection Project, you'll need to have the following software installed:

- Python 3.x
- OpenCV
- Face Recognition library

You can install the required libraries using pip:

```
pip install opencv-python face_recognition
```

## Usage
1. Clone the repository or download the source code.
2. Place a known image of the person you want to recognize in the `img/` directory.
3. Run the `face_detection.py` script:

```
python face_detection.py
```

4. The application will start the webcam and display the video feed with face detection and recognition.
5. Press the 'Q' key to quit the application.

## How It Works
1. The `face_detection.py` script starts by loading the known face image from the `img/` directory using the `face_recognition.load_image_file()` function.
2. It then encodes the known face using the `face_recognition.face_encodings()` function, which generates a numerical representation of the face.
3. The script then starts the webcam and repeatedly captures frames from the video stream.
4. For each frame, it uses the `face_recognition.face_locations()` function to detect the locations of any faces in the frame.
5. It then uses the `face_recognition.face_encodings()` function to generate numerical representations of the detected faces.
6. Finally, it compares the detected face encodings to the known face encoding using the `face_recognition.compare_faces()` function, and displays the name of the recognized person (or "Unknown" if not recognized) on the video feed.

## Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/LeGiT300/NCM/).

## Credits
- [OpenCV](https://opencv.org/) - The open-source computer vision library used for image and video processing.
- [Face Recognition](https://github.com/ageitgey/face_recognition) - The library used for face detection and recognition.

## License
This project is licensed under the [MIT License](LICENSE).
