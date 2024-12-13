import json

def restore_all_books(all_books):
    with open("all_books.json", "r") as fp:
        all_books = json.load(fp)
    return all_books

def restore_lended_books(all_lended_books):
    with open("all_lended_books.json", "r") as fp:
        all_lended_books = json.load(fp)
    return all_lended_books