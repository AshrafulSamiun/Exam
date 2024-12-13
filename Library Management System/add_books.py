from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    # isbn = int(input("Enter ISBN Number: "))



    while True:
        try:
            year = int(input("Enter Publishing Year Number: "))
            if year <= 0:
                raise ValueError("The Publishing Year must be positive.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid Year.")

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            if quantity <= 0:
                raise ValueError("The Quantity must be positive.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            price = int(input("Enter Book Price: "))
            if price <= 0:
                raise ValueError("The Price must be positive.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    
    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books Added Successully")
    
    return all_books
    