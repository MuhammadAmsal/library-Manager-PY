import json

# Load existing library or create a new one
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

# Function to add a book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    save_library(library)
    print("Book added successfully!\n")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            print("Book removed successfully!\n")
            return
    print("Book not found.\n")

# Function to search for a book
def search_book(library):
    query = input("Enter book title or author to search: ").lower()
    
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]
    
    if results:
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    else:
        print("No matching books found.")
    print()

# Function to display all books
def display_books(library):
    if not library:
        print("No books in the library.\n")
        return
    
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
    print()

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("No books in the library.\n")
        return
    
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100
    
    print(f"Total books: {total_books}")
    print(f"Books read: {read_books} ({read_percentage:.2f}%)\n")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("Personal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()


1