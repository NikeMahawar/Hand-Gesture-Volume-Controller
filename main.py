import cv2
import math
import mediapipe as mp
import pyautogui

volume_step = 2
prev_distance = 0
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_x = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x * frame.shape[1]
            thumb_y = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].y * frame.shape[0]
            index_x = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]
            index_y = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0]
            distance = int(math.sqrt((thumb_x - index_x) ** 2 + (thumb_y - index_y) ** 2))

            if prev_distance == 0:
                prev_distance = distance
            if distance > prev_distance + 10:
                pyautogui.press("volumeup", presses=volume_step)
                prev_distance = distance
            elif distance < prev_distance - 10:
                pyautogui.press("volumedown", presses=volume_step)
                prev_distance = distance

    cv2.imshow("Hand Volume Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
