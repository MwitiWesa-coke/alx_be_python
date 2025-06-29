class Book:
    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Look for the first available book with the given title and check it out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        """
        Look for a checked-out book with the given title and return it.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'.")
                return
        print(f"'{title}' was not checked out from this library.")

    def list_available_books(self):
        """
        Print all books that are not checked out.
        """
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
