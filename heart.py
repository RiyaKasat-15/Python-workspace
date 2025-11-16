import cv2
import mediapipe as mp
import random2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, image = cap.read()
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # process the data
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            # print(results.multi_hand_landmarks)

            # for checking left or right hand
            for hand in results.multi_handedness:
                # print(hand)
                hands_type = hand.classification[0].label

            # Draw hand
            for hand_landmarks in results.multi_hand_landmarks:

                # print(hand_landmarks)
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                if hands_type == "Right":
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)):
                        cv2.putText(image, "BTS HEART LOL", (110, 80), cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (0, 0, 255), 3, cv2.LINE_AA)
                        cv2.putText(image, "HEHEHE", (250, 120), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2, cv2.LINE_AA)
                if hands_type == "Left":
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x)):
                        cv2.putText(image, "BTS HEART LOL", (110, 80), cv2.FONT_HERSHEY_SIMPLEX, 2,
                                    (0, 0, 255), 3, cv2.LINE_AA)
                        cv2.putText(image, "HEHEHE", (250, 120), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows
