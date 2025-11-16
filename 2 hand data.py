import cv2
import mediapipe as mp
import random2

# helps us draw detections on to the opencv image
mp_drawing = mp.solutions.drawing_utils

# importing holistic model, we use hand (many in mediapipe)
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# assign accuracy, tracking confidence
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, image = cap.read()
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB fpr mediapipe.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # process the data
        results = hands.process(image)

        # displays class...we need to access specific function to obtain data
        # print(results)

        # You get 21 total landmarks 0-20(if every landmark is in frame)
        # print(results.multi_hand_landmarks)

        # for checking left or right hand
        # print(results.multi_handedness)
        hands_type = ""

        # check if hand
        if results.multi_hand_landmarks:
            # gives error if no hand

            for hand in results.multi_handedness:
                # print(hand)

                # can explain seqentially with dataset striping
                hands_type = hand.classification[0].label
                # print(hands_type)
            # openCV needs bgr
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # esc ASCII 27
        if cv2.waitKey(1) & 0xFF == 27:
            break
        cv2.imshow('Cam Feed', image)
cap.release()
cv2.destroyAllWindows
