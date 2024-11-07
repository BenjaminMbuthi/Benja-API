# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False  # Book is already borrowed

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False  # Book was not borrowed

# Define the LibraryMember class
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            if book.mark_as_borrowed():
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book.title}' by {book.author}")
            else:
                print(f"Could not borrow '{book.title}' - it is already borrowed.")
        else:
            print(f"'{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.mark_as_returned():
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book.title}' by {book.author}")
            else:
                print(f"Could not return '{book.title}' - it was not marked as borrowed.")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Initialize some books and a library member
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("1984", "George Orwell")
book3 = Book("Moby Dick", "Herman Melville")

member = LibraryMember("Benjamin", "M001")

# Interactive flow for borrowing and returning books
def borrow_return_flow():
    while True:
        action = input("\nEnter 'borrow' to borrow a book, 'return' to return a book, 'list' to view borrowed books, or 'exit' to quit: ").strip().lower()
        if action == "borrow":
            book_title = input("Enter the title of the book you want to borrow: ").strip()
            book = next((b for b in [book1, book2, book3] if b.title == book_title), None)
            if book:
                member.borrow_book(book)
            else:
                print(f"The book '{book_title}' is not available in the library.")
        elif action == "return":
            book_title = input("Enter the title of the book you want to return: ").strip()
            book = next((b for b in member.borrowed_books if b.title == book_title), None)
            if book:
                member.return_book(book)
            else:
                print(f"The book '{book_title}' is not in your borrowed list.")
        elif action == "list":
            member.list_borrowed_books()
        elif action == "exit":
            print("Exiting the library system.")
            break
        else:
            print("Invalid action. Please try again.")

borrow_return_flow()
