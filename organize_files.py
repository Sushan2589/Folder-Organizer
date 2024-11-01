import os
import shutil
from pathlib import Path

def organize_files(directory):
    # Dictionary to map file extensions to folder names
    extension_map = {
        # Images
        '.jpg': 'Images', '.jpeg': 'Images', '.png': 'Images', '.gif': 'Images',
        # # Documents
        '.pdf': 'Documents', '.doc': 'Documents', '.docx': 'Documents', '.txt': 'Documents',
        # # Audio
        '.mp3': 'Audio', '.wav': 'Audio', '.flac': 'Audio',
        # # Video
        '.mp4': 'Videos', '.avi': 'Videos', '.mkv': 'Videos',
        # # Archives
        '.zip': 'Archives', '.rar': 'Archives', '.7z': 'Archives',
        # Code
        '.py': 'Code', '.js': 'Code', '.html': 'Code', '.css': 'Code',
    }

    # Convert directory to Path object
    directory = Path(directory)

    # Create folders if they don't exist
    for folder in set(extension_map.values()):
        folder_path = directory / folder
        folder_path.mkdir(exist_ok=True)

    # Organize files
    for file_path in directory.iterdir():
        # Skip if it's a directory
        if file_path.is_dir():
            continue

        # Get the file extension
        file_extension = file_path.suffix.lower()

        # Skip if no extension or not in our mapping
        if not file_extension or file_extension not in extension_map:
            continue

        # Get the destination folder
        destination_folder = directory / extension_map[file_extension]

        # Create the destination path
        destination = destination_folder / file_path.name

        # Move the file
        try:
            shutil.move(str(file_path), str(destination))
            print(f"Moved {file_path.name} to {extension_map[file_extension]}")
        except Exception as e:
            print(f"Error moving {file_path.name}: {e}")

if __name__ == "__main__":
    # Get the directory to organize from user input
    directory = input("Enter the directory path to organize: ")
    
    # Check if directory exists
    if os.path.exists(directory):
        organize_files(directory)
        print("\nOrganization complete!")
    else:
        print("Directory not found!")
