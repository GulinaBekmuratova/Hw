import os

def write_to_file(file, body):
    if os.path.isfile(f"{file}"):
        with open(f"{file}", 'w') as filee:
            filee.write(f"{body}")
            filee.close()
        print(f"Текст: '{body}' записан в {file}")
    else:
        print("Такого файла не существует")
