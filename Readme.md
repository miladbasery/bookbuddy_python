# 📚 BookBuddy: ردیاب کتابخانه شخصی

`BookBuddy` یک برنامه خط فرمان (CLI) ساده است که با پایتون ساخته شده تا به شما در پیگیری عادات مطالعه، ثبت پیشرفت و مدیریت کتابخانه شخصی‌تان کمک کند.

---

## 🚀 ویژگی‌های کلیدی

* **افزودن کتاب:** ثبت کتاب‌های جدید با اطلاعات ضروری (عنوان، نویسنده، ژانر، تعداد صفحات).
* **پشتیبانی از وراثت:** امکان افزودن انواع مختلف کتاب (کتاب چاپی، کتاب الکترونیکی، کتاب صوتی) با ویژگی‌های منحصربه‌فرد.
* **ثبت مطالعه:** ثبت جلسات مطالعه (تعداد صفحات خوانده شده، یادداشت‌ها).
* **گزارش پیشرفت:** مشاهده درصد پیشرفت و وضعیت مطالعه برای هر کتاب.
* **مشاهده کتابخانه:** نمایش تمام کتاب‌های موجود در کتابخانه.
* **ذخیره و بازیابی:** امکان **Export** (خروجی گرفتن) و **Import** (وارد کردن) داده‌های کتابخانه با فرمت‌های **JSON** یا **Pickle**.
* **لاگ‌برداری:** ثبت تمام فعالیت‌های کاربر و خطاهای احتمالی در یک فایل `bookbuddy.log`.

---

## 🛠️ معماری پروژه

این پروژه از یک معماری ماژولار برای جداسازی مسئولیت‌ها (Separation of Concerns) استفاده می‌کند:

bookbuddy/ ├── config/ │ └── logger.py # تنظیمات مربوط به لاگ‌برداری ├── models/ │ ├── book.py # کلاس پایه Book │ ├── ebook.py # کلاس EBook با وراثت از Book │ ├── audiobook.py # کلاس AudioBook با وراثت از Book │ └── reading_log.py # کلاس ReadingLog ├── services/ │ ├── reading_tracker.py # منطق اصلی برنامه (افزودن، یافتن، ثبت) │ └── progress_manager.py # منطق مربوط به محاسبه و نمایش پیشرفت ├── storage/ │ ├── json_handler.py # خواندن و نوشتن فایل‌های JSON │ ├── pickle_handler.py # خواندن و نوشتن فایل‌های Pickle │ └── data_exporter.py # مدیریت فرآیند ایمپورت و اکسپورت ├── utils/ │ └── decorators.py # دکوراتورها (مانند log_activity) └── main.py # فایل اصلی اجرایی و رابط کاربری (CLI)


---

## ⚙️ نحوه اجرا

این پروژه فقط از کتابخانه‌های استاندارد پایتون استفاده می‌کند و نیازی به نصب پکیج جداگانه ندارد.

1.  مطمئن شوید که پایتون 3 (نسخه 3.7 یا بالاتر) روی سیستم شما نصب است.
2.  ترمینال (یا Command Prompt) خود را باز کنید.
3.  با دستور `cd` به پوشه‌ای بروید که پوشه `bookbuddy` در آن قرار دارد.
4.  برنامه را با دستور زیر اجرا کنید:

    ```bash
    python bookbuddy/main.py
    ```
    *(توجه: اگر از پایتون 3 در کنار نسخه 2 استفاده می‌کنید، ممکن است نیاز باشد از `python3` به جای `python` استفاده کنید.)*

---

## 🖥️ نمونه خروجی

پس از اجرا، با منوی اصلی مواجه خواهید شد:

📚 Welcome to BookBuddy! Track your reading, log progress, and manage your personal library.

Main Menu:

Add a new book

View all books

Log reading progress

View reading progress

Export book data

Import book data

Exit

Enter your choice (1-7): 1


### افزودن کتاب جدید

📘 Add a New Book
Enter book title: Atomic Habits Enter author name: James Clear Enter genre: Self-help Enter total pages: 320

✅ Book 'Atomic Habits' added successfully!

Returning to main menu... (Press Enter)


### مشاهده پیشرفت

📈 Reading Progress:
Atomic Habits - 40/320 pages read (12.5%)

Returning to main menu... (Press Enter)