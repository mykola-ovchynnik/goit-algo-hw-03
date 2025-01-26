import os
import shutil
import sys


def parse_arguments():
    if len(sys.argv) < 2:
        print(
            "Please, follow this pattern: python recursion.py <source_dir> [<dest_dir>]"
        )
        sys.exit(1)
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir) or not os.path.isdir(source_dir):
        print(
            f"Error: Source directory '{source_dir}' does not exist or is not a directory."
        )
        sys.exit(1)

    return source_dir, dest_dir


def copy_file(source_path, dest_dir, file_extension):
    try:
        dest_path = os.path.join(dest_dir, file_extension)
        os.makedirs(dest_path, exist_ok=True)
        shutil.copy2(
            source_path, os.path.join(dest_path, os.path.basename(source_path))
        )
    except Exception as e:
        print(f"Error copying file {source_path}: {e}")


def copy_files_recursive(source_dir, dest_dir):
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            if os.path.isdir(source_path):
                copy_files_recursive(source_path, dest_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:] or "unknown"
                copy_file(source_path, dest_dir, file_extension)
    except Exception as e:
        print(f"Error processing {source_dir}: {e}")


if __name__ == "__main__":
    source_directory, destination_directory = parse_arguments()
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    copy_files_recursive(source_directory, destination_directory)
