import cv2
import mediapipe as mp


# helps us draw detections on to the opencv image
mp_drawing = mp.solutions.drawing_utils

# importing holistic model, we use hand (many in mediapipe)
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, image = cap.read()

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    # esp ASCII 27
    if cv2.waitKey(1) & 0xFF == 27:
        break
    cv2.imshow('Cam Feed', image)
cap.release()
cv2.destroyAllWindows
