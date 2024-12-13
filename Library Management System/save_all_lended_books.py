
import json

def save_all_lended_books(all_lended_book):
    with open("all_lended_books.json", "w") as fp:
        json.dump(all_lended_book, fp, indent=4)