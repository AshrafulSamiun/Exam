import view_all_contacts
import add_contacts
import delete_contact
import search_contact
import csv

print("Welcome to Contact Book Management System")
all_contact=[]
try:
    with open("all_contact_lists.csv", "r") as file:
        file_reader = csv.reader(file)
        has_data = False
        index=0
        for row in file_reader:
            contact = {
                "name": row[0],
                "email": row[1],
                "contact_no": row[2],
                "address": row[3]
            }
            all_contact.append(contact)
            has_data = True
            index+=1
            if index==1:
                print("Contact Book List:")
            print(f"Name: {row[0]} | Email: {row[1]} | Phone Number: {row[2]} | Address: {row[3]} ")

        if not has_data:
            print("No Contact Found in Contact Book Management System")
except FileNotFoundError:
    print("The file 'all_contact_lists.csv' was not found.")


while True:

    print("0. Exit")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    menu=input("Select Any Number: ")

    if menu=="0":
        print("Thanks for Using Contact Book Management System")
        break
    elif menu=="1":
        all_contact=add_contacts.add_contact(all_contact)
        #print("Contact Added Successfully ")
    elif menu=="2":
        view_all_contacts.display_contact()
        print("Contact displayed Successfully")
    elif menu=="3":
        serching_option = input("Enter Searching info")
        filter_contact=search_contact.filter(serching_option)

    elif menu=="4":
        contact_no = input("Enter Contact Number").strip()
        all_books=delete_contact.remove_contact(all_contact,contact_no)
        print("Contact Deleted Successfully")
    else:
        print("Chose a Valid Number ")