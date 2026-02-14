import mediapipe as mp
import cv2

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

def detect_two_fingers(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if not result.multi_hand_landmarks:
        return False

    hand = result.multi_hand_landmarks[0]
    fingers = []

    # index & middle finger
    fingers.append(hand.landmark[8].y < hand.landmark[6].y)
    fingers.append(hand.landmark[12].y < hand.landmark[10].y)

    return fingers.count(True) == 2
