import os
import csv
from zipfile import ZipFile

from pypdf import PdfReader

from script_os import RESOURCES_DIR

files = [
    f"{RESOURCES_DIR}/text.pdf",
    f"{RESOURCES_DIR}/book.xlsx",
    f"{RESOURCES_DIR}/users.csv"
]


def create_zip_archive(file_paths):
    # Создаем ZIP-архив
    with ZipFile("resources/archive.zip", 'w') as zip_file:
        for file_path in file_paths:
            # Добавляем каждый файл в архив
            if os.path.isfile(file_path):
                zip_file.write(file_path, os.path.basename(file_path))
            else:
                return f"Файл {file_path} не существует."


def read_pdf(file_path):
    with ZipFile('resources/archive.zip') as zip_file:
        if file_path not in zip_file.namelist():
            assert False, f"Файл {file_path} не найден в архиве."

        with zip_file.open(file_path) as pdf_file:
            reader = PdfReader(pdf_file)
            return reader.pages[0].extract_text()


def read_csv(file_path):
    with ZipFile('resources/archive.zip') as zip_file:
        if file_path not in zip_file.namelist():
            assert False, f"Файл {file_path} не найден в архиве."

        with zip_file.open(file_path) as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
            print(data)
            return data


def test_pdf():
    create_zip_archive(files)
    actual_text = read_pdf("text.pdf")
    assert "имя, фамилия, отчество, должность" in actual_text


def test_csv():
    create_zip_archive(files)
    actual_text = read_csv("users.csv")
    expected_text = "имя, фамилия, отчество, должность"
    found = any(expected_text in row for row in actual_text)
    assert found, f"Текст '{expected_text}' не найден в файле data.csv"

def test_exel():

