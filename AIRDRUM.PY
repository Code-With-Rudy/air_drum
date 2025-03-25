import cv2
import threading
import pygame.midi
import time
from cvzone.HandTrackingModule import HandDetector

# 🎹 Initialize Pygame MIDI
pygame.midi.init()
player = pygame.midi.Output(0)  # No need to set instrument for drums

# 🎐 Initialize Hand Detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8)

# 🥁 Drum Sounds (MIDI Percussion Mapping)
notes = {
    "left": {
        "thumb": 36,   # Bass Drum
        "index": 38,   # Snare Drum
        "middle": 42,  # Closed Hi-Hat
        "ring": 46,    # Open Hi-Hat
        "pinky": 49    # Crash Cymbal
    },
    "right": {
        "thumb": 51,   # Ride Cymbal
        "index": 37,   # Side Stick
        "middle": 39,  # Hand Clap
        "ring": 41,    # Floor Tom
        "pinky": 45    # Low Tom
    }
}

# Sustain Time (No sustain needed for drums)
SUSTAIN_TIME = 0

# Track Previous States to Stop Notes
prev_states = {hand: {finger: 0 for finger in notes[hand]} for hand in notes}

# 🎵 Function to Play a Drum Sound
def play_drum(note):
    player.write_short(0x99, note, 127)  # 0x99 = Note On for Channel 9
    time.sleep(0.1)  # Short hit duration
    player.write_short(0x89, note, 127)  # 0x89 = Note Off for Channel 9

while True:
    success, img = cap.read()
    if not success:
        print("❌ Camera not capturing frames")
        continue

    hands, img = detector.findHands(img, draw=True)

    if hands:
        for hand in hands:
            hand_type = "left" if hand["type"] == "Left" else "right"
            fingers = detector.fingersUp(hand)
            finger_names = ["thumb", "index", "middle", "ring", "pinky"]

            for i, finger in enumerate(finger_names):
                if finger in notes[hand_type]:  # Only check assigned notes
                    if fingers[i] == 1 and prev_states[hand_type][finger] == 0:
                        threading.Thread(target=play_drum, args=(notes[hand_type][finger],), daemon=True).start()
                    prev_states[hand_type][finger] = fingers[i]  # Update state

    cv2.imshow("Hand Tracking MIDI Drums", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.midi.quit()
