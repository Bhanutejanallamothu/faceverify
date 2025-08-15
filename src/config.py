"""
Configuration file for faceverify project.
"""

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
IDS_DIR = DATA_DIR / "ids"
SELFIES_DIR = DATA_DIR / "selfies"
ENCODINGS_DIR = DATA_DIR / "encodings"
LOGS_DIR = BASE_DIR / "logs"

# Encoding settings
TOLERANCE = 0.6  # Lower = stricter match

# Camera settings
CAMERA_INDEX = 0
