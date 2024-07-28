import cv2

from src import HandDetection, HandOption

resolution_x = 1280 / 2
resolution_y = 720 / 2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution_x)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution_y)

hand_detector = HandDetection(HandOption.RIGHT_HAND)


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