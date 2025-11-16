import cv2
import mediapipe as mp
import random2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, image = cap.read()
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        hands_type = ""
        fing_total = 0
        if results.multi_hand_landmarks:

            # right or left hand
            for hand in results.multi_handedness:
                hands_type = hand.classification[0].label

            # detects & count fingers
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # To display finger names
                # fin = ''
                if hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                    val1 = 0
                else:
                    val1 = 1
                    # fin = 'Index '

                if hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    val2 = 0
                else:
                    val2 = 1
                    # fin += 'Middle '

                if hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y:
                    val3 = 0
                else:
                    val3 = 1
                    # fin += 'Ring '

                if hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y:
                    val4 = 0
                else:
                    val4 = 1
                    # fin += 'PINKY '

                if hands_type == "Right":

                    # for right thumb
                    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                        val5 = 0
                    else:
                        val5 = 1
                        # fin += 'R_THUMB '

                if hands_type == "Left":
                    # for left thumb
                    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                        val5 = 0
                    else:
                        val5 = 1
                        # fin += 'L_THUMB '
                fing_total = val1+val2+val3+val4+val5

            cv2.putText(image, str(fing_total), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        (0, 0, 255), 3, cv2.LINE_AA)
            # print(fing_total)
            # print(fin)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cv2.destroyAllWindows
