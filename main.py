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