from datetime import date
from typing import Dict, Any
from .book import Book

class EBook(Book):
    def __init__(self, title: str, author: str, genre: str, total_pages: int, 
                 file_format: str, date_added: date = None, pages_read: int = 0):
        super().__init__(title, author, genre, total_pages, date_added, pages_read, book_type="EBook")
        self.file_format = file_format

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["file_format"] = self.file_format
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EBook':
        data['date_added'] = date.fromisoformat(data['date_added'])
        data.pop('book_type', None) 
        return cls(**data)