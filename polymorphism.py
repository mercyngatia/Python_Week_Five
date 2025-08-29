# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.


class Book:

    # Instance attributes - unique to each object. A recipe for making a book
    def __init__(self, title, author, genre, pages):
        self.title = title              # book title
        self.author = author            # book author
        self.genre = genre              # book genre
        self.pages = pages              # number of pages
        self.is_borrowed = False        # Is the book currently borrowed?

       # What happens when someone wants to borrow the book?
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"You have borrowed '{self.title}'. Enjoy reading!"
        else:
            return f"Sorry, '{self.title}' is already borrowed."

        # What happens when someone returns the book?
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You have returned '{self.title}'. Thank you!"
        else:
            return f"'{self.title}' was not borrowed."
        
        # How we show information about the book
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Currently borrowed"
        return f"'{self.title}' by {self.author} - Genre: {self.genre}, Pages: {self.pages}. Status: {status}"
    

    # Making a special type of book - a Children's Book
class ChildrenBook(Book):
    def __init__(self, title, author, subject, pages):
        # Children's Book is like a regular book, but with a subject
        super().__init__(title, author, "Children's Fantasy Book", pages)
        self.subject = subject    # What the book is about
        
        # Children's Book - has a special read method
    def read_with_understanding(self):
        return f"Reading {self.subject} with no understanding about '{self.title}'..."

    # Children's Book - shows information display
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Currently borrowed"
        return f"Children's Book: '{self.title}' by {self.author} - Genre: {self.genre}, Pages: {self.pages}. About: {self.subject}. Status: {status}."

    # Example usage:
if __name__ == "__main__":
        print("Welcome to the Library!")

        # Create - regular book
        book1 = Book("1984", "George Orwell", "Dystopian", 328)
        book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 281)
        book3 = Book("Introduction to Algorithms", "Cormen et al.", "Computer Science", 1312)

        print("Our regular books:")
        print(book1)
        print(book2)
        print(book3)
        print()

        # Borrowing and returning books
        print(book1.borrow())
        print(book1.borrow())
        print(book1.return_book())
        print()
        
        # create - Children's Book
        child_book = ChildrenBook("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "Magic and Friendship", 309)

        print("Our children's book:")
        print(child_book)
        print(child_book.read_with_understanding())
        print(child_book.borrow())
        print()

        #show all books
        print("All books in the library:")
        all_books = [book1, book2, book3, child_book]
        for book in all_books:
            print(f"{book}")
        
        
        
# Activity 2: Polymorphism Challenge! 🎭
# Create a program that includes animals 
# or vehicles with the same action (like move()). However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Base class Animal
class Animal:
    def move(self):
        print("This animal is moving")

# Fish sub-class
class Fish(Animal):
    def move(self):
        print("Swimming in water")

# Bird sub-class
class Bird(Animal):
    def move(self):
        print("Flying in the sky")

# Fish sub-class
class Cow(Animal):
    def move(self):
        print("Walking on land")
        
# Snake sub-class
class Snake(Animal):
    def move(self):
        print("Slithering on the ground")

# Create a list of different animals
animals = [Fish(), Bird(), Cow(), Snake()]

# Loop through each animal and call its move method
for a in animals:
    a.move()
