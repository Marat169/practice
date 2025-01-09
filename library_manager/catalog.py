class Library:
    def __init__(self):
        """Инициализирует экземпляр библиотеки с пустым списком книг."""

        self.books = []

    def add_book(self, title, author, genre):
        """Добавляет книгу в библиотеку."""
        self.books.append({"title": title, "author": author, "genre": genre})

    def delete_book(self, title):
        """Удаляет книгу по названию."""
        self.books = [book for book in self.books if book["title"] != title]

    def search_book(self, **kwargs):
        """Ищет книги по заданным критериям."""
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if book.get(key) == value]
        return results

    def view_all_books(self):
        """Возвращает все книги в библиотеке."""
        return self.books
