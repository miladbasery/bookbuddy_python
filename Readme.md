# 📚 BookBuddy: Personal Library Tracker

`BookBuddy` is a simple Command-Line Interface (CLI) application built with Python to help you track your reading habits, log your progress, and effortlessly manage your personal library.

---

## 🚀 Key Features

* **Add Books:** Register new books with essential details (title, author, genre, total pages).
* **Inheritance Support:** Add different formats of books (Print, E-Book, AudioBook), each with their own unique attributes.
* **Reading Logs:** Record reading sessions, including the number of pages read and personal notes.
* **Progress Reports:** View your reading status and completion percentage for each book.
* **View Library:** Display a comprehensive list of all books currently in your library.
* **Save & Restore:** **Export** and **Import** your library data using **JSON** or **Pickle** formats.
* **Activity Logging:** Automatically track user actions and potential errors in a `bookbuddy.log` file.

---

## 🛠️ Project Architecture

This project utilizes a modular architecture to ensure a clear Separation of Concerns:

```text
bookbuddy/
├── config/
│   └── logger.py            # Logging configuration
├── models/
│   ├── book.py              # Base Book class
│   ├── ebook.py             # EBook class (inherits from Book)
│   ├── audiobook.py         # AudioBook class (inherits from Book)
│   └── reading_log.py       # ReadingLog class
├── services/
│   ├── reading_tracker.py   # Core application logic (add, search, log)
│   └── progress_manager.py  # Logic for calculating and displaying progress
├── storage/
│   ├── json_handler.py      # Reading and writing JSON files
│   ├── pickle_handler.py    # Reading and writing Pickle files
│   └── data_exporter.py     # Import/Export process management
├── utils/
│   └── decorators.py        # Python decorators (e.g., @log_activity)
└── main.py                  # Main executable script and CLI entry point
```

⚙️ How to Run
This project relies entirely on Python's standard libraries and does not require any external packages to be installed.

Ensure that Python 3 (version 3.7 or higher) is installed on your system.

Open your terminal or command prompt.

Use the cd command to navigate to the directory containing the bookbuddy folder.

Run the application using the following command:

Bash
python bookbuddy/main.py
(Note: If you have Python 3 installed alongside Python 2, you may need to use python3 instead of python.)
