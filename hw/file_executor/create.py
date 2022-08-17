import os
from pathlib import Path

def create_file(file_name, extension):
    if os.path.isfile(f"{file_name}{extension}"):
        print('Такой файл уже существует!')
    else:
        location = open(f"{file_name}{extension}", 'w')
        location.close()
        print(Path(f"{file_name}{extension}").absolute())