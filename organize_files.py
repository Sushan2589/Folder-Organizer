import os
import shutil
from pathlib import Path

def organize_files(directory):
    # Dictionary to map file extensions to folder names
    extension_map = {
       '.doc': 'Text', '.docx': 'Text', '.pdf': 'Text', '.rtf': 'Text', '.tex': 'Text', '.wpd': 'Text', '.txt': 'Text',
        '.aif': 'Audio', '.cda': 'Audio', '.mp3': 'Audio', '.mpa': 'Audio', '.ogg': 'Audio', '.wav': 'Audio',
        '.wma': 'Audio', '.wpl': 'Audio', '.7z': 'Compressed files', '.arj': 'Compressed files',
        '.deb': 'Compressed files', '.pkg': 'Compressed files', '.rar': 'Compressed files', '.rpm': 'Compressed files',
        '.gz': 'Compressed files', '.z': 'Compressed files', '.zip': 'Compressed files', '.bin': 'Disc and media',
        '.dmg': 'Disc and media', '.iso': 'Disc and media', '.toast': 'Disc and media', '.vcd': 'Disc and media',
        '.csv': 'Data and database', '.dat': 'Data and database', '.db': 'Data and database',
        '.dbf': 'Data and database', '.log': 'Data and database', '.mdb': 'Data and database',
        '.sav': 'Data and database', '.sql': 'Data and database', '.tar': 'Data and database',
        '.xml': 'Data and database', '.apk': 'Executable files', '.bat': 'Executable files', '.cgi': 'Executable files',
        '.com': 'Executable files', '.exe': 'Executable files', '.gadget': 'Executable files',
        '.jar': 'Executable files', '.msi': 'Executable files', '.py': 'Programming files', '.wsf': 'Executable files',
        '.ai': 'Images', '.bmp': 'Images', '.gif': 'Images', '.ico': 'Images', '.jpeg': 'Images', '.jpg': 'Images',
        '.png': 'Images', '.ps': 'Images', '.psd': 'Images', '.svg': 'Images', '.tif': 'Images', '.tiff': 'Images',
        '.css': 'Internet related files', '.aspx': 'Internet related files', '.asp': 'Internet related files',
        '.html': 'Internet related files', '.htm': 'Internet related files', '.js': 'Internet related files',
        '.jsp': 'Internet related files', '.php': 'Internet related files', '.xhtml': 'Internet related files',
        '.key': 'Presentations', '.odp': 'Presentations', '.pps': 'Presentations', '.ppt': 'Presentations',
        '.pptx': 'Presentations', '.c': 'Programming files', '.pl': 'Programming files', '.class': 'Programming files',
        '.cpp': 'Programming files', '.cs': 'Programming files', '.h': 'Programming files', '.lnk': 'Shortcuts',
        '.java': 'Programming files', '.sh': 'Programming files', '.swift': 'Programming files',
        '.vb': 'Programming files', '.ods': 'Spreadsheet files', '.xls': 'Spreadsheet files',
        '.xlsm': 'Spreadsheet files', '.xlsx': 'Spreadsheet files', '.avi': 'Video', '.3g2': 'Video', '.3gp': 'Video',
        '.flv': 'Video', '.h264': 'Video', '.m4v': 'Video', '.mkv': 'Video', '.mov': 'Video', '.mp4': 'Video',
        '.mpg': 'Video', '.mpeg': 'Video', '.rm': 'Video', '.swf': 'Video', '.vob': 'Video', '.wmv ': 'Video'
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
