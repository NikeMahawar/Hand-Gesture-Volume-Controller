# Hand-Gesture-Volume-Controller

This Python script uses the MediaPipe and OpenCV libraries to control the system volume using hand gestures detected from a webcam feed. It calculates the distance between the thumb tip and index finger tip to adjust the volume accordingly.

Prerequisites
Python 3.x
OpenCV (pip install opencv-python)
Mediapipe (pip install mediapipe)
PyAutoGUI (pip install pyautogui)
Usage
Clone the repository:
```
git clone https://github.com/yourusername/hand-gesture-volume-control.git
cd hand-gesture-volume-control
```
Instructions
Hold your hand in front of the webcam with your thumb and index finger extended.
Move your thumb closer to or farther away from your index finger to increase or decrease the volume, respectively.
To exit the program, press 'q' on your keyboard.
Customization
You can modify the volume_step variable to change the step size of volume adjustments.

Credits
[OpenCV](https://pypi.org/project/opencv-python/)
[MediaPipe](https://pypi.org/project/mediapipe/)
[PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
