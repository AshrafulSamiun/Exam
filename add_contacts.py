import save_all_contacts
import validation




def add_contact(all_contacts):
    # ===============contact name========================
    name=validation.input_contact_name("Enter Contact Name")
    email=validation.input_email("Enter Email Address")
    contact_no=validation.input_contact_number("Enter Phone Number")
    address=validation.input_address("Enter Address")
    contact={
        "name":name,
        "email": email,
        "contact_no": str(contact_no),
        "address": address
    }
    all_contacts.append(contact)
    save_all_contacts.save_contacts(all_contacts)
    print("Contact Added Successfully")
    return all_contacts
