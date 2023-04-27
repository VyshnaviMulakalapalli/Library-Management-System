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

    def test_check_overdue_books(self):
        """Test check_overdue_books method."""
        overdue_books = self.library.check_overdue_books()
        expected_result = 1
        self.assertEqual(overdue_books, expected_result)

    def test_save_user(self):
        """Test save_user method."""
        # Create a new User object and save it to the file
        user1 = User("johndoe", "password123", "Borrower")
        user1.save()

        # Check if the user is saved correctly in the file
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user1.username:
                    self.assertEqual(row[1], user1.password)
                    self.assertEqual(row[2], user1.role)

    # Edit the user's account details and check if it's updated in the file
    def test_edit_user(self):
        """Test edit_account method."""
        user1 = User("johndoe", "password123", "Borrower")
        user1.save()
        user1.edit_account("janedoe", "newpassword", "Librarian")

        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == user1.username:
                    self.assertEqual(row[1], user1.password)
                    self.assertEqual(row[2], user1.role)
                elif row[0] == "janedoe":
                    self.assertEqual(row[1], "newpassword")
                    self.assertEqual(row[2], "Librarian")

    # Delete the user's account and check if it's removed from the file
    def test_delete_user(self):
        """Test delete_account method."""
        user1 = User("johndoe", "password123", "Borrower")
        user1.save()
        user1.delete_account()

        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.assertNotEqual(row[0], user1.username)

    def test_calculate_fine(self):
        """Test calculate_fine method."""
        user1 = User("Vyshnavi", "vyshnavi", "librarian")
        fines = user1.calculate_fine(user1.username)
        expected_result = 0.5
        self.assertEqual(fines, expected_result)

    def test_search_books(self):
        """Test search_books method."""
        title_or_author_name = "BTS"
        actual_result = len(self.library.search_books(title_or_author_name))
        expected_result = 2
        self.assertEqual(actual_result, expected_result)

    def test_recommend_books(self):
        """Test recommend_books method."""
        interest = ["Fiction"]
        result = self.library.recommend_books(interest)
        actual_result = []
        for book in result:
            actual_result.append(book.title)
        expected_result = ["Alchemist", "Harry Potter"]
        self.assertEqual(actual_result, expected_result)