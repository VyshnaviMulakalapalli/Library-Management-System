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

    def load_users(self):
        """
        Loads user data from the 'users.csv' file and returns a list of User objects.
        Parameters: None
        Returns: users (list): A list of User objects.
        """
        users = []
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                user = User(row[0], row[1], row[2])
                users.append(user)
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
        role = input("Enter your role:(librarian or borrower)")
        user = User(username, password, role)
        user.save()
        self.users.append(user)
        print("User created successfully!")
