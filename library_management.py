import csv


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


# User class
class User:
    def __init__(self, username, password, role):
        """
        Initializes a new instance of the User class with the specified username, password, and role.

        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        role (str): The role of the user, either 'Librarian' or 'Borrower'.

        Returns:
        None
        """
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        """
        Saves the current user object to the 'users.csv' file.
        Parameters: None
        Returns:None
        """
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, self.password, self.role])

class Library:
    """Represents a library with a catalog of books and a list of registered users."""

    def __init__(self):
        """
        Initializes a new instance of the Library class with an empty list of books and loads user data from the 'users.csv' file.
        Parameters: None
        Returns:None
        """
        self.books = []
        self.users = self.load_users()
    def login(self):
        """
        Authenticates and authorizes the user by checking their username, password, and role against the data in the 'users.csv' file.
        Parameters: None
        Returns: user (User): The User object corresponding to the authenticated user, or None if authentication fails.
        """
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        role = input("Enter your role:(librarian or borrower)")

        for user in self.users:
            if user.username == username and user.password == password and user.role == role:
                print(f"Login successful! Welcome, {user.username}!")
                return user

        print("Invalid username or password.")
        return None

    def checkout_book(self, borrower):
        """
        Displays the list of available books and prompts the borrower to select a book to checkout. If the selected
        book is not available, an error message is displayed.
        Parameters:borrower (str): The name of the borrower.
        Returns: None
        """
        print("Books available for checkout:")
        for i, book in enumerate(self.books):
            if book.borrower is None:
                print(f"{i + 1}. {book.title} by {book.author}")
        book_index = int(input("Enter the number of the book you want to checkout (or 0 to cancel): ")) - 1
        if book_index == -1:
            return
        if book_index < 0 or book_index >= len(self.books):
            print("Invalid book number.")
            return
        if self.books[book_index].borrower is not None:
            print("This book is already checked out.")
            return
        self.books[book_index].borrower = borrower
        print("Book checked out successfully!")

    def return_book(self, borrower):
        """
        Displays the list of books checked out by the borrower and prompts the borrower to select a book to return. If
        the selected book is not checked out by the borrower, an error message is displayed.
        Parameters:
        borrower (str): The name of the borrower.
        Returns: None
        """
        print("Books currently checked out by you:")
        for i, book in enumerate(self.books):
            if book.borrower == borrower:
                print(f"{i + 1}. {book.title} by {book.author}")
        book_index = int(input("Enter the number of the book you want to return (or 0 to cancel): ")) - 1
        if book_index == -1:
            return
        if book_index < 0 or book_index >= len(self.books):
            print("Invalid book number.")
            return
        if self.books[book_index].borrower != borrower:
            print("This book is not checked out by you.")
            return
        self.books[book_index].borrower = None
        print("Book returned successfully!")

