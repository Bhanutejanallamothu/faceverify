"""
Encodes a student ID card face.
"""
from pathlib import Path
from . import config, utils, face_db

def encode_id(student_id: str, id_image_filename: str):
    image_path = config.IDS_DIR / id_image_filename
    encoding = utils.load_and_encode(image_path)
    face_db.save_encoding(encoding, student_id, config.ENCODINGS_DIR)
