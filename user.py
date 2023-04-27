import csv
import datetime
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

    def edit_account(self, new_username, new_password, new_role):
        """
        Edits the user's account with the specified new username, password, and role.

        Parameters:
        new_username (str): The new username to set for the user.
        new_password (str): The new password to set for the user.
        new_role (str): The new role to set for the user, either 'Librarian' or 'Borrower'.

        Returns: None
        """
        current_user = None
        updated_users = []
        with open('users.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.username:
                    current_user = row
                    updated_users.append([new_username, new_password, new_role])
                else:
                    updated_users.append(row)

        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in updated_users:
                writer.writerow(row)

        self.username = new_username
        self.password = new_password
        self.role = new_role

    def delete_account(self):
        """Deletes the user's account from the 'users.csv' file."""
        with open('users.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row[0] != self.username]

        with open('users.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Account deleted successfully")

    def calculate_fine(self, borrower):
        """
        Calculates the fine for a borrower based on the number of days the borrower has held each book checked out.
        Parameters:
        borrower (str): The name of the borrower to calculate the fine for.
        Returns:
        fine (float): The total fine owed by the borrower.
        """
        fine = 0.0
        with open('checked_out_books.csv', mode='r') as checked_out_file:
            reader = csv.reader(checked_out_file)
            for row in reader:
                if row[3] == borrower:
                    # book_title = row[0]
                    checkout_date = datetime.datetime.strptime(row[4], '%Y-%m-%d').date()
                    days_checked_out = (datetime.date.today() - checkout_date).days
                    if days_checked_out > 14:
                        fine += (days_checked_out - 14) * 0.25
        print(f"Total fine for {borrower}: ${fine:.2f}")
        return fine
