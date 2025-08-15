"""
Captures a live selfie and saves it.
"""
from pathlib import Path
from . import config, camera

def capture_selfie(student_id: str):
    save_path = config.SELFIES_DIR / f"{student_id}_selfie.jpg"
    camera.capture_image(save_path)
    return save_path
