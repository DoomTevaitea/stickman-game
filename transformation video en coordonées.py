import cv2
import mediapipe as mp

# Initialiser MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5)

# Fonction pour capturer et traiter les frames vidéo
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Conversion de l'image en RGB pour MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
        
        # Extraire les coordonnées des mains
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, _ = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(f'Landmark {id}: x={cx}, y={cy}')
                    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Remplacer 'path_to_video.mp4' par le chemin de votre vidéo
process_video('path_to_video.mp4')

