# Book class

class Book:
    """Represents a book with a title, author, and genre."""

    def __init__(self, title, author, genre, borrower=None):
        """
        Initializes a new instance of the Book class with the specified title, author, genre, and optional borrower.
        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        genre (str): The genre of the book.
        borrower (str, optional): The name of the borrower who has checked out the book.

        Returns:
        None
        """
        self.title = title
        self.author = author
        self.genre = genre
        self.borrower = borrower
        self.reserved = False
        self.reserved_by = None