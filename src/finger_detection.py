from finger_option import FingerOption

class FingerDetection:
    def __init__(self, name: FingerOption):
        self.__name = name
        self.__coordinates = []
        self.__finger_init = self.__init_finger(name)
        self.__isUp = False

    @staticmethod
    def finger_detection(landmark):
        return {
            1:FingerOption.THUMB,
            2:FingerOption.THUMB,
            3:FingerOption.THUMB,
            4:FingerOption.THUMB,
            5:FingerOption.INDEX_FINGER,
            6:FingerOption.INDEX_FINGER,
            7:FingerOption.INDEX_FINGER,
            8:FingerOption.INDEX_FINGER,
            9:FingerOption.MIDDLE_FINGER,
            10:FingerOption.MIDDLE_FINGER,
            11:FingerOption.MIDDLE_FINGER,
            12:FingerOption.MIDDLE_FINGER,
            13:FingerOption.RING_FINGER,
            14:FingerOption.RING_FINGER,
            15:FingerOption.RING_FINGER,
            16:FingerOption.RING_FINGER,
            17:FingerOption.LITTLE_FINGER,
            18:FingerOption.LITTLE_FINGER,
            19:FingerOption.LITTLE_FINGER,
            20:FingerOption.LITTLE_FINGER,
        }[landmark]
    
    def add_coordinate(self, x):
        self.__coordinates.append(x)

    def reset_coordinates(self):
        self.__coordinates = []

    def check_got_up(self):
        if self.__coordinates == []:
            return False

        if self.__name == FingerOption.THUMB:
            self.__isUp = True if self.__coordinates[3][0] <= self.__coordinates[2][0] else False
        else:
            self.__isUp = True if self.__coordinates[3][1] < self.__coordinates[2][1] else False
        
        return self.__isUp

    def __init_finger(self, option):
        return {
            FingerOption.THUMB: 1,
            FingerOption.INDEX_FINGER: 5,
            FingerOption.MIDDLE_FINGER: 9,
            FingerOption.RING_FINGER: 13,
            FingerOption.LITTLE_FINGER: 17,
        }[option]