"""
Command-line interface for faceverify.
"""
import argparse
from . import encode_id, capture_selfie, verify

def main():
    parser = argparse.ArgumentParser(description="Face verification CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Enroll command
    enroll_parser = subparsers.add_parser("enroll", help="Encode a student ID card")
    enroll_parser.add_argument("student_id", help="Student ID")
    enroll_parser.add_argument("id_image", help="Image filename in data/ids")

    # Verify command
    verify_parser = subparsers.add_parser("verify", help="Verify student by selfie")
    verify_parser.add_argument("student_id", help="Student ID")

    args = parser.parse_args()

    if args.command == "enroll":
        encode_id.encode_id(args.student_id, args.id_image)
    elif args.command == "verify":
        selfie_path = capture_selfie.capture_selfie(args.student_id)
        matched, distance = verify.verify(args.student_id, selfie_path.name)
        print(f"Match: {matched}, Distance: {distance:.4f}")

if __name__ == "__main__":
    main()
