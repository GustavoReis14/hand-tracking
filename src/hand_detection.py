import mediapipe as mp
import cv2

from hand_option import HandOption
from hand import Hand

class HandDetection:
    def __init__(self, RESOLUTION_X, RESOLUTION_Y):
        self.__is_hand_detected = False
        self.__dic_hands = {
            HandOption.LEFT_HAND.value:  Hand(HandOption.LEFT_HAND, RESOLUTION_X, RESOLUTION_Y),
            HandOption.RIGHT_HAND.value: Hand(HandOption.RIGHT_HAND, RESOLUTION_X, RESOLUTION_Y)
        }

        #Media Pipe
        self.__mp_hands = mp.solutions.hands
        self.__mp_draw = mp.solutions.drawing_utils
        self.__hands = self.__mp_hands.Hands()
        

    def get_finger_values(self):
        if self.__is_hand_detected == False:
            return

        hands = []

        for hand in self.__dic_hands.values():
            fingers_up = []
            for finger in hand.get_fingers():
                fingers_up.append(finger.check_got_up())
            hands.append(fingers_up)
        
        return hands


    def process(self, frame):
        result = self.__hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if result.multi_hand_landmarks:
            self.__is_hand_detected = True
            for hand in self.__dic_hands.values():
                hand.clear_last_coordinates()

            for hand_side, landmark in zip(result.multi_handedness, result.multi_hand_landmarks):
                hand = self.__dic_hands[hand_side.classification[0].label]
                hand.set_landmark(landmark.landmark)
                hand.run()

                self.__mp_draw.draw_landmarks(frame, landmark, self.__mp_hands.HAND_CONNECTIONS)
        else:
            self.__is_hand_detected = False

                    
    
