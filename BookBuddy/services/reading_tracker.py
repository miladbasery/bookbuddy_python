from typing import List, Optional, Dict, Any
from models.book import Book
from models.ebook import EBook
from models.audiobook import AudioBook
from models.reading_log import ReadingLog

class ReadingTracker:
    def __init__(self):
        self.books: List[Book] = []
        self.logs: List[ReadingLog] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_all_books(self) -> List[Book]:
        return self.books

    def find_book(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def log_reading(self, title: str, pages_read: int, notes: str):
        book = self.find_book(title)
        if not book:
            raise ValueError(f"Book with title '{title}' not found.")
        
        book.update_progress(pages_read)
        log_entry = ReadingLog(book_title=book.title, pages_read=pages_read, notes=notes)
        self.logs.append(log_entry)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "books": [book.to_dict() for book in self.books],
            "logs": [log.to_dict() for log in self.logs]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ReadingTracker':
        tracker = cls()
        book_data_list = data.get("books", [])
        log_data_list = data.get("logs", [])

        for book_data in book_data_list:
            book_type = book_data.get("book_type", "Book")
            if book_type == "EBook":
                tracker.books.append(EBook.from_dict(book_data))
            elif book_type == "AudioBook":
                tracker.books.append(AudioBook.from_dict(book_data))
            else:
                tracker.books.append(Book.from_dict(book_data))
                
        for log_data in log_data_list:
            tracker.logs.append(ReadingLog.from_dict(log_data))
            
        return tracker