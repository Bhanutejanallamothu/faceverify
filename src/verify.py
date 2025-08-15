"""
Compares ID card face encoding with a live selfie encoding.
"""
import face_recognition
from . import config, utils, face_db

def verify(student_id: str, selfie_filename: str):
    id_encoding = face_db.load_encoding(student_id, config.ENCODINGS_DIR)
    selfie_path = config.SELFIES_DIR / selfie_filename
    selfie_encoding = utils.load_and_encode(selfie_path)

    results = face_recognition.compare_faces([id_encoding], selfie_encoding, tolerance=config.TOLERANCE)
    distance = face_recognition.face_distance([id_encoding], selfie_encoding)[0]
    return results[0], distance
