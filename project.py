class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower = None

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))

    def remove_book(self, book):
        self.books.remove(book)

    def borrow_book(self, book, borrower):
        if book.is_borrowed:
            print("Sorry, this book is already borrowed.")
        else:
            book.is_borrowed = True
            book.borrower = borrower
            print("Book borrowed successfully.")

    def return_book(self, book):
        book.is_borrowed = False
        book.borrower = None
        print("Book returned successfully.")

    def search_books(self, search_term):
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower() or search_term.lower() in book.isbn:
                results.append(book)
        return results

    def list_books(self):
        for book in self.books:
            if book.is_borrowed:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn}) - Borrowed by {book.borrower}")
            else:
                print(f"{book.title} by {book.author} (ISBN: {book.isbn})")

library = Library()

while True:
    print("\nWelcome to the Library Management System!")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. List Books")
    print("7. Exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        library.add_book(title, author, isbn)
        print("Book added successfully.")
    elif choice == "2":
        isbn = input("ISBN: ")
        book_to_remove = None
        for book in library.books:
            if book.isbn == isbn:
                book_to_remove = book
                break
        if book_to_remove:
            library.remove_book(book_to_remove)
            print("Book removed successfully.")
        else:
            print("Book not found.")
    elif choice == "3":
        isbn = input("ISBN: ")
        borrower = input("Borrower: ")
        book_to_borrow = None
        for book in library.books:
            if book.isbn == isbn:
                book_to_borrow = book
                break
        if book_to_borrow:
            library.borrow_book(book_to_borrow, borrower)
        else:
            print("Book not found.")
    elif choice == "4":
        isbn = input("ISBN: ")
        book_to_return = None
        for book in library.books:
            if book.isbn == isbn:
                book_to_return = book
                break
        if book_to_return:
            library.return_book(book_to_return)
        else:
            print("Book not found.")
    elif choice == "5":
        search_term = input("Search term: ")
        search_results = library.search_books(search_term)
        if len(search_results) == 0:
            print("No books found.")
        else:
            print("Search Results:")
            

