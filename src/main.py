import cv2
import os
from tkinter import Tk, filedialog
from datetime import datetime
import face_recognition
import numpy as np

# Paths for saving files
ID_SAVE_DIR = r"D:\face\faceverify\data\ids"
SELFIE_SAVE_DIR = r"D:\face\faceverify\data\selfies"

os.makedirs(ID_SAVE_DIR, exist_ok=True)
os.makedirs(SELFIE_SAVE_DIR, exist_ok=True)

def capture_image(save_path):
    cap = cv2.VideoCapture(0)
    print("Press SPACE to capture, ESC to cancel.")
    while True:
        ret, frame = cap.read()
        cv2.imshow("Capture", frame)
        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            cv2.imwrite(save_path, frame)
            print(f"Saved image to {save_path}")
            break

    cap.release()
    cv2.destroyAllWindows()

def upload_image(save_path):
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select Student ID Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if file_path:
        with open(file_path, "rb") as src, open(save_path, "wb") as dst:
            dst.write(src.read())
        print(f"Copied file to {save_path}")
    else:
        print("No file selected.")
        exit()

def compare_faces(id_path, selfie_path):
    try:
        id_image = face_recognition.load_image_file(id_path)
        selfie_image = face_recognition.load_image_file(selfie_path)

        id_encodings = face_recognition.face_encodings(id_image)
        selfie_encodings = face_recognition.face_encodings(selfie_image)

        if not id_encodings:
            print("❌ No face found in Student ID image.")
            return False
        if not selfie_encodings:
            print("❌ No face found in Selfie image.")
            return False

        match = face_recognition.compare_faces([id_encodings[0]], selfie_encodings[0])[0]
        distance = np.linalg.norm(id_encodings[0] - selfie_encodings[0])

        print(f"Face distance score: {distance:.4f}")
        return match

    except Exception as e:
        print(f"Error during face comparison: {e}")
        return False

if __name__ == "__main__":
    # Step 1: Capture or upload ID
    print("Select Student ID option:")
    print("1. Capture live")
    print("2. Upload from file")
    choice = input("Enter choice (1/2): ").strip()

    id_filename = f"student_id_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    id_save_path = os.path.join(ID_SAVE_DIR, id_filename)

    if choice == "1":
        capture_image(id_save_path)
    elif choice == "2":
        upload_image(id_save_path)
    else:
        print("Invalid choice.")
        exit()

    # Step 2: Capture selfie
    print("\nNow let's take a selfie...")
    selfie_filename = f"selfie_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    selfie_save_path = os.path.join(SELFIE_SAVE_DIR, selfie_filename)
    capture_image(selfie_save_path)

    # Step 3: Compare faces
    print("\nVerifying identity...")
    if compare_faces(id_save_path, selfie_save_path):
        print("✅ Face Match: ID verified successfully.")
    else:
        print("❌ Face Mismatch: ID verification failed.")
