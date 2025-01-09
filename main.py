from library_manager.catalog import Library
from library_manager.utils.data_validation import validate_author_and_title
from library_manager.utils.formatting import format_book_data
from library_manager.report import generate_report

if __name__ == "__main__":
    library = Library()

    # Добавляем книги
    library.add_book("Шерлок Холмс: Собака Баскервилей", "Артур Конан Дойл", "Детектив")
    library.add_book("The Catcher in the Rye", "J.D. Salinger", "Classic")

    # Генерация отчёта
    generate_report(library)

    # Проверка данных книги
    book_data = {"title": "Ненаписанный роман", "author": "Марат Вековищев", "genre": "детектив"}
    if validate_author_and_title(book_data):
        library.add_book(**book_data)
    else:
        print("Некорректные данные книги!")

    # Форматирование данных для вывода
    for book in library.view_all_books():
        print(format_book_data(book))

