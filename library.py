import csv

from book import Book
from user import User


## Library class
class Library:
    """Represents a library with a catalog of books and a list of registered users."""

    def __init__(self):
        """
        Initializes a new instance of the Library class with an empty list of books and loads user data from the 'users.csv' file.
        Parameters: None
        Returns:None
        """
        self.books = []
        self.load_books()
        self.users = self.load_users()

    def add_book(self):
        """
        Prompts the user to enter the details of a book and adds the book to the catalog.
        Returns:None
        """
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        genre = input("Enter the genre of the book: ")

        book = Book(title, author, genre)
        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    def remove_book(self):
        """
        Prompts the user to enter the title of a book and removes the book from the catalog, if it is not checked out.
        Returns: None
        """
        title = input("Enter the title of the book to remove: ")
        for i, book in enumerate(self.books):
            if book.title == title:
                if book.borrower is not None:
                    print("This book is currently checked out and cannot be removed.")
                else:
                    del self.books[i]
                    self.save_books()
                    print("Book removed successfully!")
                return
        print("Book not found.")

    def load_users(self):
        """
        Loads user data from the 'users.csv' file and returns a list of User objects.
        Parameters: None
        Returns: users (list): A list of User objects.
        """
        users = []
        with open('users.csv', mode='r') as user_file:
            reader = csv.reader(user_file)
            for row in reader:
                if row:  # check if row is not empty
                    try:
                        user = User(row[0], row[1], row[2])
                        users.append(user)
                    except IndexError:
                        print(f"Error loading user data: {row}")
        return users

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

    def signup(self):
        """
        Creates a new User object with the user's specified username, password, and role, and saves it to the 'users.csv' file.
        Parameters:None
        Returns: None
        """
        while True:
            username = input("Enter a username: ")
            # Check if the username already exists
            for user in self.users:
                if user.username == username:
                    print("Username already exists. Please choose a different username.")
                    break
            else:
                break
        password = input("Enter a password: ")
        while True:
            role = input("Enter your role (librarian or borrower): ")
            if role not in ["librarian", "borrower"]:
                print("Invalid role. Please enter either 'librarian' or 'borrower'.")
            else:
                break
        user = User(username, password, role)
        user.save()
        self.users.append(user)
        print("User created successfully!")

    def load_books(self):
        """Load book data from a CSV file and append it to the books list."""
        with open('books.csv', mode='r') as book_file:
            reader = csv.reader(book_file)
            # next(reader)  # skip header row
            for row in reader:
                try:
                    book = Book(row[0], row[1], row[2])
                    self.books.append(book)
                except IndexError:
                    print(f"Error loading book data: {row}")

    def save_books(self):
        """
        Saves the current state of the self.books list to the 'books.csv' file.
        Parameters: None
        Returns: None
        """
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for book in self.books:
                writer.writerow([book.title, book.author, book.genre])

    def search_books(self, query):
        """
        Searches for books in the library catalog by title or author and returns a list of books that match the query.
        Parameters:
        query (str): The search query to match against book titles and authors.
        Returns:
        books (list): A list of books that match the query.
        """
        books = []
        with open('books.csv', mode='r') as book_file:
            reader = csv.reader(book_file)
            # next(reader)  # skip header row
            for row in reader:
                title = row[0]
                author = row[1]
                if query.lower() in title.lower() or query.lower() in author.lower():
                    book = Book(title, author, row[2])
                    print(f"{book.title}, {book.author}, {book.genre}")
                    books.append(book)
        return books

    def save_checked_out_books(self):
        """
        Saves the data of all checked out books to the 'checked_out_books.csv' file.
        Parameters: None
        Returns: None
        """
        with open('checked_out_books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Author', 'Genre', 'Borrower'])
            for book in self.books:
                if book.borrower is not None:
                    writer.writerow(
                        [book.title, book.author, book.genre, book.borrower])

    def reserve_book(self, user, title):
        """
        Reserves a book that is currently checked out by setting the 'reserved' attribute to True
        and setting the 'reserved_by' attribute to the user who requested the reservation.
        If the book is not checked out, sets the 'borrower' attribute to the user who requested the reservation.

        Parameters:
        user (User): The user who requested the reservation.
        title (str): The title of the book to reserve.

        Returns:
        None
        """
        for book in self.books:
            if book.title == title:
                if book.borrower is not None:
                    book.reserved = True
                    book.reserved_by = user
                    print("Book reserved successfully!")
                else:
                    book.borrower = user
                    print("Book checked out successfully!")
                self.save_books()
                self.save_checked_out_books()
                return
        print("Book not found.")

    def recommend_books(self, interests):
        """
        Recommends books to the user based on their interests.

        Parameters:
        interests (list): A list of genres or keywords that the user is interested in.

        Returns:
        recommended_books (list): A list of books that match the user's interests.
        """
        recommended_books = []
        for book in self.books:
            for interest in interests:
                if interest.lower() in book.genre.lower() or interest.lower() in book.title.lower():
                    recommended_books.append(book)
                    break
        return recommended_books
