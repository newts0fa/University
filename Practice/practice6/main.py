import os
import sys

# Убедимся, что необходимые библиотеки установлены
try:
    import PyPDF2
    from docx import Document
except ImportError:
    # Установка необходимых библиотек
    os.system(f"{sys.executable} -m pip install PyPDF2 python-docx")
    import PyPDF2
    from docx import Document

def pdf_to_doc(pdf_file, doc_file):
    """
    Преобразование PDF в DOC.
    :param pdf_file: Путь к исходному PDF-файлу.
    :param doc_file: Путь для сохранения результата в DOC.
    """
    try:
        # Чтение PDF-файла
        reader = PyPDF2.PdfReader(pdf_file)
        document = Document()

        # Извлечение текста со страниц PDF
        for page in reader.pages:
            text = page.extract_text()
            if text.strip():  # Проверяем, есть ли текст на странице
                document.add_paragraph(text)

        # Сохранение результата в DOC-файле
        document.save(doc_file)
        print(f"PDF успешно преобразован в DOC: {doc_file}")

    except Exception as e:
        print(f"Ошибка при преобразовании PDF в DOC: {e}")

# Пример использования
if name == "__main__":
    pdf_file_path = "sample.pdf"  # Путь к PDF-файлу
    doc_file_path = "output.docx"  # Путь к выходному DOC-файлу
    
    # Проверяем существование PDF-файла
    if not os.path.exists(pdf_file_path):
        print(f"Файл {pdf_file_path} не найден. Проверьте путь.")
    else:
        pdf_to_doc(pdf_file_path, doc_file_path)
