import csv
from zipfile import ZipFile

import openpyxl
import pytest
from pypdf import PdfReader

from confest import create_zip_archive


def read_file(file_path):
    with ZipFile('resources/archive.zip') as zip_file:
        if file_path not in zip_file.namelist():
            assert False, f"Файл {file_path} не найден в архиве."

    if ".pdf" in file_path:
        with ZipFile('resources/archive.zip') as zip_file:
            with zip_file.open(file_path, "r") as pdf_file:
                # Читаем данные из файла
                reader = PdfReader(pdf_file)
                return reader.pages[0].extract_text()

    elif ".csv" in file_path:
        with ZipFile("resources/archive.zip") as zip_file:
            with zip_file.open(file_path) as file:
                # Декодируем файл
                content = file.read().decode('utf-8')
                # Читаем данные из файла
                reader = csv.reader(content.splitlines())
                text = []
                for row in reader:
                    text.append(row)
                actual_result = ', '.join([', '.join(row) for row in text])
                return actual_result

    elif ".xlsx" in file_path:
        with ZipFile("resources/archive.zip") as zip_file:
            with zip_file.open(file_path) as file:
                # Загружаем рабочую книгу
                workbook = openpyxl.load_workbook(file)

                # Выбираем активный лист (можно указать конкретный лист по имени или индексу)
                sheet = workbook.active

                # Читаем данные из листа
                text = []
                for row in sheet.iter_rows(values_only=True):
                    text.append(row)
                actual_result = ', '.join([', '.join(row) for row in text])
                return actual_result

    else:
        return f"Расширение файла {file_path} не поддреживается."


@pytest.mark.parametrize("file", [
    "text.pdf",
    "users.csv",
    "book.xlsx"
])
def test_archive(create_zip_archive, file):
    actual_result = read_file(file)
    expected_result = "имя, фамилия, отчество, должность"
    assert expected_result in actual_result, f"Текст не содержит '{expected_result}'"
