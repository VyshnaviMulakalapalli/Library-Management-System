
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
                    print("6. Reserve Book")
                    print("7. Get book recommendation")
                    print("8. Notify overdue books")
                    print("9. Calculate fines")
                    print("10. Edit account")
                    print("11. Delete account")
                    print("12. Log out")
                    librarian_choice = input("Enter your choice: ")
                    if librarian_choice == "1":
                        title = input("Enter the title of the book: ")
                        author = input("Enter the author of the book: ")
                        genre = input("Enter the genre of the book: ")
                        library.add_book(title, author, genre)
                    elif librarian_choice == "2":
                        title = input("Enter the title of the book to remove: ")
                        library.remove_book(title)
                    elif librarian_choice == "3":
                        borrower_name = user_type.username
                        library.checkout_book(borrower_name)
                    elif librarian_choice == "4":
                        borrower_name = user_type.username
                        library.return_book(borrower_name)
                    elif librarian_choice == "5":
                        title_or_author = input("Enter book title or author name: ")
                        library.search_books(title_or_author)
                    elif librarian_choice == "6":
                        title = input("Enter book title name to reserve: ")
                        user = user_type.username
                        library.reserve_book(user, title)
                    elif librarian_choice == "7":
                        interests = input("Enter your interests (separated by commas): ").split(",")
                        recommended_books = library.recommend_books(interests)
                        if len(recommended_books) == 0:
                            print("No books found.")
                        else:
                            print(f"Recommended books:")
                            for book in recommended_books:
                                print(f"- {book.title} by {book.author} ({book.genre})")
                    elif librarian_choice == "8":
                        borrower_name = user_type.username
                        library.check_overdue_books(borrower_name)
                    elif librarian_choice == "9":
                        borrower_name = user_type.username
                        user.calculate_fine(borrower_name)
                    elif librarian_choice == "10":
                        new_username = input("Enter your username: ")
                        new_password = input("Enter your password: ")
                        new_role = input("Enter your role:(librarian or borrower)")
                        user.edit_account(new_username, new_password, new_role)
                    elif librarian_choice == "11":
                        user.delete_account()
                        break

                    elif librarian_choice == "12":
                        break

                    else:
                        print("Invalid choice. Please try again.")

            elif user_type.role == "borrower":
                while True:
                    print("\n----- Borrower Options -----")
                    print("1. Checkout Book")
                    print("2. Return Book")
                    print("3. Search Books")
                    print("4. Reserve Books")
                    print("5. Get book recommendation")
                    print("6. Notify overdue books")
                    print("7. Calculate fines")
                    print("8. Edit account")
                    print("9. Delete account")
                    print("10. Logout")
                    borrower_choice = input("Enter your choice: ")
                    if borrower_choice == "1":
                        borrower_name = user_type.username
                        library.checkout_book(borrower_name)
                    elif borrower_choice == "2":
                        borrower_name = user_type.username
                        library.return_book(borrower_name)
                    elif borrower_choice == "3":
                        title_or_author = input("Enter book title or author name: ")
                        library.search_books(title_or_author)
                    elif borrower_choice == "4":
                        title = input("Enter book title name to reserve: ")
                        user = user_type.username
                        library.reserve_book(user, title)
                    elif borrower_choice == "5":
                        interests = input(
                            "Enter your interests (separated by commas): ").split(
                            ",")
                        recommended_books = library.recommend_books(interests)
                        if len(recommended_books) == 0:
                            print("No books found.")
                        else:
                            print(f"Recommended books:")
                            for book in recommended_books:
                                print(
                                    f"- {book.title} by {book.author} ({book.genre})")
                    elif borrower_choice == "6":
                        borrower_name = user_type.username
                        library.check_overdue_books(borrower_name)
                    elif borrower_choice == "7":
                        borrower_name = user_type.username
                        user.calculate_fine(borrower_name)
                    elif borrower_choice == "8":
                        new_username = input("Enter your username: ")
                        new_password = input("Enter your password: ")
                        new_role = input("Enter your role:(librarian or borrower)")
                        user.edit_account(new_username, new_password, new_role)
                    elif borrower_choice == "9":
                        user.delete_account()
                        break
                    elif borrower_choice == "10":
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
