import mediapipe as mp
import cv2

from hand_option import HandOption
from finger_option import FingerOption
from finger_detection import FingerDetection

class HandDetection:
    def __init__(self, hand_option: HandOption, RESOLUTION_X, RESOLUTION_Y):
        self.__RESOLUTION_X = RESOLUTION_X
        self.__RESOLUTION_Y = RESOLUTION_Y
        
        self.__is_hand_detected = False
        self.__hand_option = hand_option

        #Media Pipe
        self.__mp_hands = mp.solutions.hands
        self.__mp_draw = mp.solutions.drawing_utils
        self.__hands = self.__mp_hands.Hands()

        self.__wrist = []
        self.__fingers = {
            FingerOption.THUMB: FingerDetection(FingerOption.THUMB),
            FingerOption.INDEX_FINGER: FingerDetection(FingerOption.INDEX_FINGER),
            FingerOption.MIDDLE_FINGER: FingerDetection(FingerOption.MIDDLE_FINGER),
            FingerOption.RING_FINGER: FingerDetection(FingerOption.RING_FINGER),
            FingerOption.LITTLE_FINGER: FingerDetection(FingerOption.LITTLE_FINGER),
        }

    def get_finger_values(self):
        if self.__is_hand_detected == False:
            return

        fingers_up = []

        for finger in self.__fingers.values():
            fingers_up.append(finger.check_got_up())
        
        return fingers_up


    def process(self, frame):
        result = self.__hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if result.multi_hand_landmarks:
            self.__is_hand_detected = True
            self.__clear_last_fingers_coordinates()

            for hand_side, landmark in zip(result.multi_handedness, result.multi_hand_landmarks):
                if(hand_side.classification[0].label != self.__hand_option.value):
                    continue

                for index, point in enumerate(landmark.landmark):
                    x, y, z = int(point.x * self.__RESOLUTION_X), int(point.y * self.__RESOLUTION_Y), int(point.z * self.__RESOLUTION_X)

                    if index == 0:
                        self.__wrist.append((x, y, z))
                    else:
                        finger = self.__fingers[FingerDetection.finger_detection(index)]
                        finger.add_coordinate((x, y, z))

                self.__mp_draw.draw_landmarks(frame, landmark, self.__mp_hands.HAND_CONNECTIONS)
        else:
            self.__is_hand_detected = False

                    
    def __clear_last_fingers_coordinates(self):
        for finger in self.__fingers.values():
            finger.reset_coordinates()      

