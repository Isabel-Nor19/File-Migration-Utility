import os 
import shutil
import tkinter as tk
from tkinter import filedialog

FILE_MAP = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", "heic", "heif"],
    "Zip_Files": [".zip", ".tar", ".gz"],
    "Installers": [".dmg", ".pkg", ".exe", ".msi"],
    "Programs": [".py", ".java"],
    "Powerpoints": [".pptx"]
}

# user selects file path
def user_selection():
    root = tk.Tk()
    root.withdraw
    file_path = filedialog.askdirectory(title="Select Folder to Organise")
    return file_path

    

def clean_files(file_path):
    if os.path.exists(file_path):
        for f in os.listdir(file_path):
            # print(f)
            full_path = os.path.join(file_path, f)
            # print(full_path)
            if os.path.isfile(full_path):
                # print(f)
                name, ext = os.path.splitext(full_path)
                ext = ext.lower()

                for folder_name, extensions in FILE_MAP.items():
                    if ext in extensions:
                        target_folder = os.path.join(file_path, folder_name)

                        if not os.path.exists(target_folder):
                            os.makedirs(target_folder)

                        shutil.move(full_path, os.path.join(target_folder, f))
                        break
            
    else:
        raise FileNotFoundError('file path does not exist')
    

    # print(os.listdir(file_path))




if __name__ == '__main__':
    print("Starting organization...")
    chosen_path = user_selection()
    clean_files(chosen_path)
    print("Done...")
