from datetime import date
from typing import Dict, Any
from .book import Book

class AudioBook(Book):
    def __init__(self, title: str, author: str, genre: str, total_pages: int, 
                 narrator: str, date_added: date = None, pages_read: int = 0):
        super().__init__(title, author, genre, total_pages, date_added, pages_read, book_type="AudioBook")
        self.narrator = narrator

    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["narrator"] = self.narrator
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AudioBook':
        data['date_added'] = date.fromisoformat(data['date_added'])
        data.pop('book_type', None)
        return cls(**data)