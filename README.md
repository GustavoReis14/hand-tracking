
# Hand and Finger Detection Project

This project uses MediaPipe and OpenCV to detect hands and infer finger positions in real-time from video capture. The goal is to process the camera image, identify hands, and determine which fingers are raised.

## Project Structure

```
project_root/
│
├── main.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── hand_detection.py
│   ├── finger_detection.py
│   ├── hand.py
│   ├── hand_option.py
│   └── finger_option.py
```

## Dependencies

Make sure you have Python 3.x installed. The necessary dependencies are listed in the `requirements.txt` file.

### Installing Dependencies

```sh
pip install -r requirements.txt
```

## Running the Project

To run the project, use the following command:

```sh
export PYTHONPATH=src:$PYTHONPATH
python3 main.py
```

## Main Files

### main.py

This is the main file that starts the video capture and uses the `HandDetection` class to process each frame.

```python
import cv2
from src import HandDetection

RESOLUTION_X = 1280 / 2
RESOLUTION_Y = 720 / 2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION_X)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION_Y)

hand_detector = HandDetection(RESOLUTION_X, RESOLUTION_Y)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    hand_detector.process(frame)
    fingers = hand_detector.get_finger_values()
    if fingers:
        print(fingers)
    
    cv2.imshow('Hand Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### src/hand_detection.py

Implements the hand detection logic using MediaPipe.

### src/finger_detection.py

Implements the finger detection logic and determines if a specific finger is raised.

### src/hand.py

Defines the `Hand` class, which manages the finger positions of a specific hand.

### src/hand_option.py

Defines the hand options (right and left) using an enum.

```python
from enum import Enum

class HandOption(Enum):
    RIGHT_HAND = 'Right'
    LEFT_HAND  = 'Left'
```

### src/finger_option.py

Defines the finger options using an enum.

```python
from enum import Enum

class FingerOption(Enum):
    THUMB         = 'Thumb'
    INDEX_FINGER  = 'Index Finger'
    MIDDLE_FINGER = 'Middle Finger'
    RING_FINGER   = 'Ring Finger'
    LITTLE_FINGER = 'Little Finger'
```

## Contribution

Feel free to contribute to the project. You can do so by opening issues or submitting pull requests. Before contributing, please read the `CONTRIBUTING.md` file.

## License

This project is licensed under the MIT license. See the `LICENSE` file for more information.