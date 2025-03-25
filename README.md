# air_drum

Virtual Drum Kit Using Hand Tracking 🥁🎵
Description
This Python project allows you to play a virtual drum kit using hand gestures. It leverages OpenCV, cvzone's Hand Tracking Module, and Pygame MIDI to detect finger movements and trigger drum sounds in real-time. No physical drum set is required—just your webcam and some hand gestures!

How It Works
Uses OpenCV to capture real-time video input from your webcam.

Detects hand gestures using cvzone's HandTrackingModule.

Maps different fingers to specific MIDI drum sounds.

Sends MIDI signals through Pygame MIDI to produce drum sounds.

Multi-threading ensures seamless note triggering.

Features
✅ Real-time hand tracking using OpenCV and cvzone.
✅ MIDI-based drumming with finger gestures.
✅ Different fingers trigger different drum sounds (Snare, Bass, Hi-Hat, etc.).
✅ No sustain for natural drum hits.
✅ Threaded note playing for lag-free performance.
✅ Simple UI with OpenCV window displaying hand tracking.

Drum Sound Mapping
Hand	Finger	MIDI Drum Sound
Left	Thumb	Bass Drum (36)
Left	Index	Snare Drum (38)
Left	Middle	Closed Hi-Hat (42)
Left	Ring	Open Hi-Hat (46)
Left	Pinky	Crash Cymbal (49)
Right	Thumb	Ride Cymbal (51)
Right	Index	Side Stick (37)
Right	Middle	Hand Clap (39)
Right	Ring	Floor Tom (41)
Right	Pinky	Low Tom (45)
Installation & Setup
1️⃣ Install Dependencies
Ensure you have Python installed, then run:

sh
Copy
Edit
pip install opencv-python cvzone pygame
2️⃣ Run the Script
sh
Copy
Edit
python hand_drums.py
3️⃣ Controls
Move fingers up/down to play drum sounds.

Press 'q' to exit the program.

Future Improvements
🚀 Add customizable drum mappings.
🚀 Support for multiple MIDI outputs.
🚀 Implement velocity-sensitive drumming.

Contributing
Feel free to contribute by submitting pull requests or reporting issues. 🎉
