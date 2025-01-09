def generate_report(library):
    """Генерирует отчёт о книгах в библиотеке."""
    books = library.view_all_books()
    if not books:
        return "Библиотека пуста."
    
    report = ["Список книг в библиотеке:"]
    for book in books:
        report.append(f"- {book['title']} (Автор: {book['author']}, Жанр: {book['genre']})")
    return "\n".join(report)
