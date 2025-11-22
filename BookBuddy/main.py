import sys
from config.logger import logger
from models.book import Book
from services.reading_tracker import ReadingTracker
from services.progress_manager import ProgressManager
from storage.data_exporter import DataExporter
from utils.decorators import log_activity

def clear_screen():
    print("\n" * 5) 

def pause():
    input("\nReturning to main menu... (Press Enter)")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            value_str = input(prompt)
            value_int = int(value_str)
            if value_int <= 0:
                print("Input must be a positive number.")
            else:
                return value_int
        except ValueError:
            print("Invalid input. Please enter a number.")

@log_activity("Add New Book")
def add_new_book(tracker: ReadingTracker):
    print("📘 Add a New Book")
    print("-" * 20)
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    total_pages = get_int_input("Enter total pages: ")
    
    book = Book(title=title, author=author, genre=genre, total_pages=total_pages)
    tracker.add_book(book)
    
    logger.info(f"Book '{title}' added.")
    print(f"\n✅ Book '{title}' added successfully!")
    pause()

@log_activity("View All Books")
def view_all_books(tracker: ReadingTracker):
    print("📚 Your Library:")
    print("-" * 20)
    books = tracker.get_all_books()
    if not books:
        print("Your library is empty.")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book}")
    pause()

@log_activity("Log Reading Progress")
def log_reading_progress(tracker: ReadingTracker):
    print("📖 Log Reading Progress")
    print("-" * 20)
    title = input("Enter book title: ")
    
    try:
        book = tracker.find_book(title)
        if not book:
            raise ValueError(f"Book '{title}' not found.")
            
        pages_read = get_int_input(f"Enter pages read (current: {book.pages_read}/{book.total_pages}): ")
        notes = input("Enter notes (optional): ")
        
        tracker.log_reading(title, pages_read, notes)
        
        logger.info(f"Logged {pages_read} pages for '{title}'.")
        print("\n✅ Reading log added!")
        
    except ValueError as e:
        print(f"\nError: {e}")
        logger.warning(f"Failed to log progress: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        logger.error(f"Unexpected error in log_reading_progress: {e}")
    pause()

@log_activity("View Reading Progress")
def view_reading_progress(tracker: ReadingTracker, manager: ProgressManager):
    print("📈 Reading Progress:")
    print("-" * 20)
    report = manager.get_progress_report(tracker)
    for line in report:
        print(line)
    pause()

@log_activity("Export Book Data")
def export_book_data(tracker: ReadingTracker, exporter: DataExporter):
    print("📤 Export Book Data")
    print("-" * 20)
    print("Choose format:")
    print("1. JSON")
    print("2. Pickle")
    
    format_choice = input("Enter choice (1-2): ")
    filename = input("Enter filename (e.g., my_books.json): ")
    
    try:
        if format_choice == '1':
            format_type = 'json'
        elif format_choice == '2':
            format_type = 'pickle'
        else:
            raise ValueError("Invalid format choice.")
            
        exporter.export_data(tracker, filename, format_type)
        print(f"\n✅ Data exported to '{filename}'")
        logger.info(f"Data exported to {filename} as {format_type}")
        
    except (ValueError, Exception) as e:
        print(f"\nError: {e}")
        logger.error(f"Export failed: {e}")
    pause()

@log_activity("Import Book Data")
def import_book_data(exporter: DataExporter) -> ReadingTracker:
    print("📥 Import Book Data")
    print("-" * 20)
    print("Choose format:")
    print("1. JSON")
    print("2. Pickle")
    
    format_choice = input("Enter choice (1-2): ")
    filename = input("Enter filename (e.g., my_books.json): ")
    
    try:
        if format_choice == '1':
            format_type = 'json'
        elif format_choice == '2':
            format_type = 'pickle'
        else:
            raise ValueError("Invalid format choice.")
            
        tracker = exporter.import_data(filename, format_type)
        print(f"\n✅ Data imported successfully from '{filename}'")
        logger.info(f"Data imported from {filename}")
        pause()
        return tracker
        
    except (ValueError, Exception) as e:
        print(f"\nError: {e}")
        logger.error(f"Import failed: {e}")
        pause()
        return None

def main_menu():
    print("📚 Welcome to BookBuddy!")
    print("Track your reading, log progress, and manage your personal library.")
    print("\nMain Menu:")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Log reading progress")
    print("4. View reading progress")
    print("5. Export book data")
    print("6. Import book data")
    print("7. Exit")
    
    return input("\nEnter your choice (1-7): ")

def main():
    tracker = ReadingTracker()
    manager = ProgressManager()
    exporter = DataExporter()
    
    while True:
        clear_screen()
        choice = main_menu()
        
        clear_screen()
        if choice == '1':
            add_new_book(tracker)
        elif choice == '2':
            view_all_books(tracker)
        elif choice == '3':
            log_reading_progress(tracker)
        elif choice == '4':
            view_reading_progress(tracker, manager)
        elif choice == '5':
            export_book_data(tracker, exporter)
        elif choice == '6':
            new_tracker = import_book_data(exporter)
            if new_tracker:
                tracker = new_tracker
        elif choice == '7':
            print("Goodbye! Happy reading! 📖")
            logger.info("Application exited.")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            pause()

if __name__ == "__main__":
    main()