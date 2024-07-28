import mediapipe as mp
import cv2

from hand_option import HandOption
from finger_option import FingerOption
from finger_detection import FingerDetection

resolution_x = 1280 / 2
resolution_y = 720 / 2

class HandDetection:
    def __init__(self, hand_option: HandOption):
        self.isHandDetected = False
        self.hand_option = hand_option
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands()
        self.wrist = []
        self.fingers = {
            FingerOption.THUMB: FingerDetection(FingerOption.THUMB),
            FingerOption.INDEX_FINGER: FingerDetection(FingerOption.INDEX_FINGER),
            FingerOption.MIDDLE_FINGER: FingerDetection(FingerOption.MIDDLE_FINGER),
            FingerOption.RING_FINGER: FingerDetection(FingerOption.RING_FINGER),
            FingerOption.LITTLE_FINGER: FingerDetection(FingerOption.LITTLE_FINGER),
        }

    def get_finger_values(self):
        print(self.hand_option.value)

    def process(self, frame):
        result = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if result.multi_hand_landmarks:
            self.isHandDetected = True
            for hand_side, landmark in zip(result.multi_handedness, result.multi_hand_landmarks):
                if(hand_side.classification[0].label != self.hand_option.value):
                    continue
                for index, point in enumerate(landmark.landmark):
                    x, y, z = int(point.x * resolution_x), int(point.y * resolution_y), int(point.z * resolution_x)
                    if index == 0:
                        self.wrist.append((x, y, z))
                    else:
                        finger = self.fingers[FingerDetection.finger_detection(index)]
                        finger.add_coordinate((x, y, z))
                self.mp_draw.draw_landmarks(frame, landmark, self.mp_hands.HAND_CONNECTIONS)
        else:
            self.isHandDetected = False

                    
                        
                    

