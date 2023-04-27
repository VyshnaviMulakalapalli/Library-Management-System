import unittest
import csv
from book import Book
from user import User
from library import Library


class LibraryTests(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("Test Book", "Test Author", "Test Genre")
        self.user = User("Alice", "1234", "borrower")

    def test_add_book(self):
        """Test add_book method."""
        # Add a book to the library
        self.library.add_book("Test Book", "Test Author", "Test Genre")

        # Assert that the book has been added to the library's catalog
        self.assertTrue(any(book.title == "Test Book" for book in self.library.books))

    def test_remove_book(self):
        """Test remove_book method."""
        # Add a book to the library
        self.library.add_book("Test Book1", "Test Author1", "Test Genre1")

        # Remove the book from the library's catalog
        self.library.remove_book("Test Book1")

        # Assert that the book has been removed from the library's catalog
        self.assertFalse(any(book.title == "Test Book1" for book in self.library.books))