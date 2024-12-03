import csv
from zipfile import ZipFile

import openpyxl
from pypdf import PdfReader
from confest import create_zip_archive
import csv
from zipfile import ZipFile

import openpyxl
from pypdf import PdfReader

from confest import create_zip_archive


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

    with ZipFile("resources/archive.zip") as zip_file:
        with zip_file.open(file_path) as file:
            content = file.read().decode('utf-8')
            reader = csv.reader(content.splitlines())
            actual_text = []
            for row in reader:
                actual_text.append(row)
            return actual_text


def read_exel(file_path):
    with ZipFile('resources/archive.zip') as zip_file:
        if file_path not in zip_file.namelist():
            assert False, f"Файл {file_path} не найден в архиве."

    with ZipFile("resources/archive.zip") as zip_file:
        with zip_file.open(file_path) as file:
            # Загружаем рабочую книгу
            workbook = openpyxl.load_workbook(file)

            # Выбираем активный лист (можно указать конкретный лист по имени или индексу)
            sheet = workbook.active

            # Читаем данные из листа
            actual_text = []
            for row in sheet.iter_rows(values_only=True):
                actual_text.append(row)
            return actual_text


def test_pdf(create_zip_archive):
    actual_text = read_pdf("text.pdf")
    expected_text = "имя, фамилия, отчество, должность"
    assert expected_text in actual_text


def test_csv(create_zip_archive):
    actual_text = read_csv("users.csv")
    expected_text = "имя, фамилия, отчество, должность"
    actual_text_str = ', '.join([', '.join(row) for row in actual_text])
    assert expected_text in actual_text_str


def test_exel(create_zip_archive):
    actual_text = read_exel("book.xlsx")
    expected_text = "имя, фамилия, отчество, должность"
    actual_text_str = ', '.join([', '.join(row) for row in actual_text])
    assert expected_text in actual_text_str
