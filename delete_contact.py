import save_all_contacts

def remove_contact(contact_list,contact_no):
    filterlist=[contact for contact in contact_list if contact['contact_no'].strip()!=contact_no]
    save_all_contacts.save_contacts(filterlist)
    return filterlist