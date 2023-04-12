
from library import Library
from user import User



# Main loop
def main():
    """Runs the main loop of the Library Management System."""
    library = Library()


    while True:
        print("\n----- Library Management System -----")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_type = library.login()
            user = User(user_type.username, user_type.password, user_type.role)
            if user_type.role == "librarian":
                while True:
                    print("\n----- Librarian Options -----")
                    print("1. Add Book")
                    print("2. Remove Book")
                    print("3. Checkout Book")
                    print("4. Return Book")
                    print("5. Search book")
                    print("6. Edit account")
                    print("7. Delete account")
                    print("8. Log out")
                    librarian_choice = input("Enter your choice: ")
                    if librarian_choice == "1":
                        library.add_book()
                    elif librarian_choice == "2":
                        library.remove_book()
                    elif librarian_choice == "3":
                        borrower_name = input("Enter borrower name: ")
                        library.checkout_book(borrower_name)
                    elif librarian_choice == "4":
                        borrower_name = input("Enter borrower name: ")
                        library.return_book(borrower_name)
                    elif librarian_choice == "5":
                        title_or_author = input("Enter book title or author name: ")
                        library.search_books(title_or_author)
                    elif librarian_choice == "6":
                        new_username = input("Enter your username: ")
                        new_password = input("Enter your password: ")
                        new_role = input("Enter your role:(librarian or borrower)")
                        user.edit_account(new_username, new_password, new_role)
                    elif librarian_choice == "7":
                        user.delete_account()

                    elif librarian_choice == "8":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif user_type.role == "borrower":
                while True:
                    print("\n----- Borrower Options -----")
                    print("1. Checkout Book")
                    print("2. Return Book")
                    print("3. Search Books")
                    print("4. Edit account")
                    print("5. Delete account")
                    print("6. Logout")
                    borrower_choice = input("Enter your choice: ")
                    if borrower_choice == "1":
                        borrower_name = input("Enter borrower name: ")
                        library.checkout_book(borrower_name)
                    elif borrower_choice == "2":
                        borrower_name = input("Enter borrower name: ")
                        library.return_book(borrower_name)
                    elif borrower_choice == "3":
                        title_or_author = input("Enter book title or author name: ")
                        library.search_books(title_or_author)
                    elif borrower_choice == "4":
                        new_username = input("Enter your username: ")
                        new_password = input("Enter your password: ")
                        new_role = input("Enter your role:(librarian or borrower)")
                        user.edit_account(new_username, new_password, new_role)
                    elif borrower_choice == "5":
                        user.delete_account()

                    elif borrower_choice == "6":
                        # library.logout()
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "2":
            library.signup()
        elif choice == "3":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
