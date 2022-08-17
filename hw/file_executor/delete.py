import os

def delete_file(file):
    if os.path.isfile(f"{file}"):
        os.remove(f"{file}")
        print(f"Файл {file} удален!!!")
    else:
        print(f"Такого файла нету")