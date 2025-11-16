import cv2
import mediapipe as mp
import random2

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


player_score = 0
bot_score = 0

player = True
bot = False


def check_status(player_score, bot_score):
    if player_score > bot_score:
        print('* * * * * * * * * * * *')
        print('* * * Player wins * * *')
        print('* * * * * * * * * * * *')

    else:
        print('* * * * * * * * * * * *')
        print('* * *  Bot wins  * * *')
        print('* * * * * * * * * * * *')


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

                    # for right 6
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x)):
                        fing_total = 6

                    # for right YO
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y)):
                        print("Quiting")
                        cap.release()

                    # for right thumb
                    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                        val5 = 0
                    else:
                        val5 = 1
                        # fin += 'R_THUMB '

                if hands_type == "Left":

                    # for left 6
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].x)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].x)):
                        fing_total = 6

                    # for left YO
                    if ((hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y)
                        & (hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y)
                            & (hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y)):
                        print("Quiting")
                        cap.release()

                    # for left thumb
                    if hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x:
                        val5 = 0
                    else:
                        val5 = 1
                        # fin += 'L_THUMB '

            if fing_total != 6:
                fing_total = val1+val2+val3+val4+val5

            cv2.putText(image, str(fing_total), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        (0, 0, 255), 3, cv2.LINE_AA)
            # print(fing_total)
            # print(fin)

        if player is True:
            cv2.putText(image, "Player bats", (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (3, 227, 252), 1, cv2.LINE_AA)
        else:
            cv2.putText(image, "Player bowls", (0, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (3, 227, 252), 1, cv2.LINE_AA)

        # Cricket game
        # press spacebar
        if cv2.waitKey(10) & 0xFF == 32:
            print(fing_total)
            cv2.putText(image, str(fing_total), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        (0, 0, 255), 3, cv2.LINE_AA)

            # print corresponding gestures which are in their ranges
            player_num = fing_total
            if player is True:  # i.e. player will bat first
                # print('Player will bat !')

                bot_num = random2.randint(0, 6)
                if player_num == bot_num:
                    print('ME-> {} - AI-> {}'.format(player_num, bot_num), end=' ')
                    print('Player is out!')
                    # print('Final score of Player: {}'.format(player_score))
                    print()
                    print()
                    print('Bot will bat now!')
                    player = False
                    bot = True

                else:
                    player_score += player_num
                    print('ME-> {} - AI-> {}'.format(player_num, bot_num), end=' ')
                    print('Player score: {}'.format(player_score))

            elif bot is True:  # i.ie if player is out, bot will bat
                bot_num = random2.randint(0, 6)

                if bot_num == player_num:
                    print('ME-> {} - AI-> {}'.format(player_num, bot_num), end=' ')
                    print('Bot is out!')
                    print()
                    print('Final score of Bot: {}'.format(bot_score))
                    print('Final score of Player: {}'.format(player_score))
                    print()
                    check_status(player_score, bot_score)
                    # resets flags
                    player = False
                    bot = True
                else:
                    bot_score += bot_num
                    print('P-> {} - AI-> {}'.format(player_num, bot_num), end=' ')
                    print('Bot score: {}'.format(bot_score))

        cv2.putText(image, "Plz press SPACEBAR to play", (160, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
