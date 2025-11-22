from datetime import date
from typing import Dict, Any

class ReadingLog:
    def __init__(self, book_title: str, pages_read: int, notes: str, log_date: date = None):
        self.book_title = book_title
        self.pages_read = pages_read
        self.notes = notes
        self.log_date = log_date or date.today()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "book_title": self.book_title,
            "pages_read": self.pages_read,
            "notes": self.notes,
            "log_date": self.log_date.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ReadingLog':
        data['log_date'] = date.fromisoformat(data['log_date'])
        return cls(**data)