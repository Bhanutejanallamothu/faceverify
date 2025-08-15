"""
Utility functions for image loading and face encoding.
"""
import face_recognition
from pathlib import Path

def load_and_encode(image_path: Path):
    """
    Load image and return face encodings.
    Raises ValueError if no face or multiple faces are found.
    """
    image = face_recognition.load_image_file(str(image_path))
    locations = face_recognition.face_locations(image)
    if len(locations) != 1:
        raise ValueError(f"Expected 1 face, found {len(locations)} in {image_path}")
    encoding = face_recognition.face_encodings(image, known_face_locations=locations)[0]
    return encoding
