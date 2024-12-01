import csv
def filter(serch_data):
    with open("all_contact_lists.csv", "r") as file:
        file_reader = csv.reader(file)
        found = False
        for row in file_reader:
            row_data=" ".join(map(str, row))
            if serch_data.lower() in row_data.lower():
                found = True
                print(f"Name: {row[0]} | Email: {row[1]} | Contact No {row[2]} | Address {row[3]} ")

        if not found:
            print(f"No Contact Found for {serch_data} in Contact Book Management System")