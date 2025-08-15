"""
Handles webcam capture for selfies.
"""
import cv2
from pathlib import Path

def capture_image(save_path: Path):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open camera")

    print("Press SPACE to capture, ESC to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Live Capture", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            cv2.imwrite(str(save_path), frame)
            print(f"Image saved to {save_path}")
            break

    cap.release()
    cv2.destroyAllWindows()
