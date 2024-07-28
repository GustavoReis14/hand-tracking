from threading import Thread
from hand_option import HandOption

from finger_option import FingerOption
from finger_detection import FingerDetection

class Hand(Thread):
    def __init__ (self, name: HandOption, RESOLUTION_X, RESOLUTION_Y):
        Thread.__init__(self)

        self.__RESOLUTION_X = RESOLUTION_X
        self.__RESOLUTION_Y = RESOLUTION_Y
        self.name = name
        self.__wrist = []
        self.__fingers = {
            FingerOption.THUMB: FingerDetection(FingerOption.THUMB),
            FingerOption.INDEX_FINGER: FingerDetection(FingerOption.INDEX_FINGER),
            FingerOption.MIDDLE_FINGER: FingerDetection(FingerOption.MIDDLE_FINGER),
            FingerOption.RING_FINGER: FingerDetection(FingerOption.RING_FINGER),
            FingerOption.LITTLE_FINGER: FingerDetection(FingerOption.LITTLE_FINGER),
        }
        self.__landmark = []
    
    
    def run(self):
        for index, point in enumerate(self.__landmark):
            x, y, z = int(point.x * self.__RESOLUTION_X), int(point.y * self.__RESOLUTION_Y), int(point.z * self.__RESOLUTION_X)

            if index == 0:
                self.__wrist.append((x, y, z))
            else:
                finger = self.__fingers[FingerDetection.finger_detection(index)]
                finger.add_coordinate((x, y, z))

    def clear_last_coordinates(self):
        self.__wrist = []
        for finger in self.__fingers.values():
            finger.reset_coordinates()     

    def  set_landmark(self, landmark):
        self.__landmark = landmark
    
    def get_fingers(self):
        return self.__fingers.values()