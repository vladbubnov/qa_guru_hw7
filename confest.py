import os
from zipfile import ZipFile

import pytest

from script_os import RESOURCES_DIR


@pytest.fixture(scope='class')
def create_zip_archive():
    files = [
        os.path.join(RESOURCES_DIR, file)
        for file in os.listdir(RESOURCES_DIR)
        if os.path.isfile(os.path.join(RESOURCES_DIR, file)) and not file.startswith('.')
    ]

    # Создаем ZIP-архив
    with ZipFile("resources/archive.zip", 'w') as zip_file:
        for file in files:
            # Добавляем каждый файл в архив
            if os.path.isfile(file):
                zip_file.write(file, os.path.basename(file))
            else:
                return f"Файл {file} не существует."

    yield

    # Удаляем созданный ZIP-архив
    if os.path.exists("resources/archive.zip"):
        if os.path.isfile("resources/archive.zip"):
            os.remove("resources/archive.zip")
