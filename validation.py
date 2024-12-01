import csv

#=======Contact Number validation & Duplicate Check
def input_contact_number(message):
    contact_no = input(message).strip()
    if not contact_no:
        print("Phone Number Must not be Empty")
        return input_contact_number("Please Enter a valid Phone Number")

    elif not contact_no.isdigit():
        print("Phone Number Must be Digit")
        return input_contact_number("Please Enter a valid Phone Number")
    # ====================Duplicate Contact No Check========================
    else:
        duplicate_contact = False
        with open("all_contact_lists.csv", "r") as file:
            file_reader = csv.reader(file)
            has_data = False
            for row in file_reader:

                if row[2].strip() == contact_no:
                    print("This Contact already Exist in the Contact List.")
                    return input_contact_number("Enter Another Phone Number")

        return contact_no



def input_contact_name(message):
    name = input(message)
    if not name:
        print("Contact Name Must not be Empty")
        return input_contact_name("Please Enter a valid Contact Name")
    elif  name.isdigit():
        print("Contact Name Must be String")
        return input_contact_name("Please Enter a valid Contact Name")
    else:
        return name.strip()


def input_email(message):
    email = input("Enter Email Address").strip()
    if  email and isinstance(email, str) and "@"  in email and "."  in email:
        return email
    else:
        return input_email("Please Enter a valid Email Address")


def input_address(message):
    address = input("Enter Address").strip()
    if not address:
        print("Address Must not be Empty")
        return input_address("Please Enter Address")
    else:
        return address


