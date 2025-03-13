import cv2
from deepface import DeepFace
import numpy as np

# Cargar emojis
emojis = {
    "happy": cv2.imread("happy_emoji.png"),
    "sad": cv2.imread("sad_emoji.png"),
    "angry": cv2.imread("angry_emoji.png")
}

# Inicializar la cámara
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        try:
            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
            emotion = analysis[0]['dominant_emotion']
            
            if "happy" in emotion:
                emoji = emojis["happy"]
            elif "sad" in emotion:
                emoji = emojis["sad"]
            elif "angry" in emotion:
                emoji = emojis["angry"]
            else:
                emoji = None
            
            if emoji is not None:
                emoji = cv2.resize(emoji, (w, h))
                frame[y:y+h, x:x+w] = emoji
        except Exception as e:
            print("Error en reconocimiento:", e)
    
    cv2.imshow("Reconocimiento de Emociones", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
