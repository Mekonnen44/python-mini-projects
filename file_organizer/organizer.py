import os
import shutil

source = "test_folder"

for file in os.listdir(source):
    if file.endswith(".txt"):
        os.makedirs("text_files", exist_ok=True)
        shutil.move(os.path.join(source, file), "text_files")