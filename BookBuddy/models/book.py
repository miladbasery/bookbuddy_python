from datetime import date
from typing import Dict, Any

class Book:
    def __init__(self, title: str, author: str, genre: str, total_pages: int, 
                 date_added: date = None, pages_read: int = 0, book_type: str = "Book"):
        self.title = title
        self.author = author
        self.genre = genre
        self.total_pages = total_pages
        self.date_added = date_added or date.today()
        self.pages_read = pages_read
        self.book_type = book_type

    def update_progress(self, pages: int):
        self.pages_read = min(self.total_pages, self.pages_read + pages)

    @property
    def progress_percentage(self) -> float:
        if self.total_pages == 0:
            return 0.0
        return (self.pages_read / self.total_pages) * 100

    @property
    def status(self) -> str:
        if self.pages_read == 0:
            return "Unread"
        elif self.pages_read >= self.total_pages:
            return "Finished"
        else:
            return "In Progress"

    def __str__(self) -> str:
        return f"{self.title} by {self.author} [{self.genre}] - {self.total_pages} pages"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "total_pages": self.total_pages,
            "date_added": self.date_added.isoformat(),
            "pages_read": self.pages_read,
            "book_type": self.book_type
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Book':
        data['date_added'] = date.fromisoformat(data['date_added'])
        return cls(**data)