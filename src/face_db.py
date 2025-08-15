"""
Manages saving and loading face encodings.
"""
import json
import numpy as np
from pathlib import Path

def save_encoding(encoding, student_id: str, save_dir: Path):
    npy_path = save_dir / f"{student_id}.npy"
    meta_path = save_dir / f"{student_id}.json"

    np.save(npy_path, encoding)
    with open(meta_path, "w") as f:
        json.dump({"student_id": student_id}, f)
    print(f"Saved encoding for {student_id}")

def load_encoding(student_id: str, save_dir: Path):
    npy_path = save_dir / f"{student_id}.npy"
    if not npy_path.exists():
        raise FileNotFoundError(f"No encoding found for {student_id}")
    return np.load(npy_path)
