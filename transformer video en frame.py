import cv2
import os

# Définir le chemin où les frames seront sauvegardées
save_path = 'image/decomposition fond'

# Créer le dossier s'il n'existe pas déjà
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Charger la vidéo
video_path = 'image/fond_ecran_video.mp4'
vidcap = cv2.VideoCapture(video_path)

success, image = vidcap.read()
count = 0

while success:
    # Construire le chemin complet pour chaque frame
    filename = f"{save_path}/frame{count}.jpg"
    cv2.imwrite(filename, image)  # sauvegarder le frame
    success, image = vidcap.read()
    count += 1