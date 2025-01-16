class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} (Available: {self.copies})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.copies > 0:
                book.copies -= 1
                print(f"You borrowed '{book.title}'. Enjoy reading!")
                return
        print("Sorry, the book is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Thank you for returning '{book.title}'.")
                return
        print("The book does not belong to this library.")

    def list_books(self):
        if not self.books:
            print("The library is empty!")
        else:
            print("Available books:")
            for book in self.books:
                print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. List All Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            copies = int(input("Enter number of copies: "))
            book = Book(title, author, copies)
            library.add_book(book)

        elif choice == '2':
            title = input("Enter the title of the book you want to borrow: ")
            library.borrow_book(title)

        elif choice == '3':
            title = input("Enter the title of the book you want to return: ")
            library.return_book(title)

        elif choice == '4':
            library.list_books()

        elif choice == '5':
            print("Thank you for using the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
