import save_all_books
import save_all_lended_books


def return_books(all_books,all_lended_book):
    search_book = input("Enter Book Title to Return: ")
    for book in all_books:
        if book["title"] == search_book:

            book['quantity'] += 1
            for lend_book in all_lended_book:
                if lend_book["title"] == search_book:
                    borrower = input("Enter Borrower Name: ")
                    if lend_book["borrowerName"]== borrower:
                        all_lended_book.remove(lend_book)
                        save_all_books.save_all_books(all_books)
                        save_all_lended_books.save_all_lended_books(all_lended_book)
                        print("Book Return Successfully")
                        return all_books, all_lended_book



    #print("Book Not Found")

