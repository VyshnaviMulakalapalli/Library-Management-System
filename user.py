import csv

# User class


class User:
    def init(self, username, password, role):
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

    def delete_account(self):
        """Deletes the user's account from the 'users.csv' file."""
        with open('users.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != self.username]

        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Account deleted successfully")