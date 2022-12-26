import os
import shutil

# Specify the directory to search for the files, /!\ every backslash needs to be doubled /!\
source_dir = 'C:\\User\\JAAJ'

# Specify the directory to copy the files to, /!\ every backslash needs to be doubled /!\
target_dir = 'E:\\Folder\\JAAJ'


for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.zip'): # Change the .zip to whatever extention you like
            source_path = os.path.join(root, file)
            shutil.copy(source_path, target_dir)
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
