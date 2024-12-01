def save_contacts(all_contacts):
    with open("all_contact_lists.csv", "w") as fp:
        for contact in all_contacts:
            line = f"{contact['name']}, {contact['email']}, {contact['contact_no']}, {contact['address']}\n"
            fp.write(line)