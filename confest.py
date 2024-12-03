import os
from zipfile import ZipFile

import pytest
from selene import browser

from script_os import RESOURCES_DIR


@pytest.fixture(scope='class')
def create_zip_archive():
    files = [
        f"{RESOURCES_DIR}/text.pdf",
        f"{RESOURCES_DIR}/book.xlsx",
        f"{RESOURCES_DIR}/users.csv"
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

    if os.path.exists("resources/archive.zip"):
        if os.path.isfile("resources/archive.zip"):
            os.remove("resources/archive.zip")
