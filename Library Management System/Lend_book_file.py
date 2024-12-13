from save_all_lended_books import save_all_lended_books
from save_all_books import save_all_books
import random
from datetime import datetime, timedelta


def lend_books(all_books,all_lended_book):
    title = input("Enter Book Title: ")
    book_available=False
    for book in all_books:
        if book['title']==title:
            if book['quantity']>0:
                book_available=True
                book['quantity']-=1
            else:
                print("No enough books are available to lend.")
                return

    if book_available:
        borrowerName = input("Enter Borrower Name: ")
        borrowerPhone= input("Enter Phone Number: ")
        bookB0rrowAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # Assume that 15 days later book need to return
        returnDate=datetime.now()+timedelta(days=15)
        bookreturnDate =returnDate.strftime("%d-%m-%Y %H:%M:%S")

        lend_book = {
            "title": title,
            "borrowerName": borrowerName,
            "borrowerPhone": borrowerPhone,
            "bookBorrowAt": bookB0rrowAt,
            "bookReturnDate": bookreturnDate
        }
        all_lended_book.append(lend_book)
        save_all_lended_books(all_lended_book)
        save_all_books(all_books)

        print("Books Lended Successully")

        return all_books
    else:
        print("No Book found")
