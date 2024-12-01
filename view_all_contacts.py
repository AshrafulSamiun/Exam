import csv

def display_contact():
    try:
        with open("all_contact_lists.csv", "r") as file:
            file_reader=csv.reader(file)
            has_data=False
            for row in file_reader:
                #print(row[0])
                has_data=True
                print(f"Name: {row[0]} | Email: {row[1]} | Phone Number: {row[2]} | Address: {row[3]} ")

            if not has_data:
                print("No Contact Found in Contact Book Management System")
    except FileNotFoundError:
        print("The file 'all_contact_lists.csv' was not found.")
    except KeyError as e:
        print(f"Missing expected column: {e}")
