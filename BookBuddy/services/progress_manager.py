from typing import List
from services.reading_tracker import ReadingTracker

class ProgressManager:
    def get_progress_report(self, tracker: ReadingTracker) -> List[str]:
        report = []
        books = tracker.get_all_books()
        if not books:
            return ["Your library is empty."]
            
        for book in books:
            report.append(
                f"{book.title} - {book.pages_read}/{book.total_pages} pages read "
                f"({book.progress_percentage:.1f}%)"
            )
        return report