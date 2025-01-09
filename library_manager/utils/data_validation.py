import requests

def validate_author_and_title(book_data):
    """Проверяет, что автор и название книги не пустые."""
    title = book_data.get("title")
    author = book_data.get("author")
    
    if not title or not author:
        print("Название и автор должны быть обязательны!")
        return False
    
    # формируем запрос к Google Books API
    url = f"https://www.googleapis.com/books/v1/volumes?q=title:{title}+inauthor:{author}"
    response = requests.get(url)
    
    if response.status_code == 200:
        books = response.json().get("items", [])
        if books:
            print(f"Книга '{title}' авторства '{author}' найдена!")
            return True
        else:
             print(f"Книга '{title}' авторства '{author}' не найдена!")
    else:
        print("Ошибка при запросе к Google Books API.")
        
    return False         
