import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()
    address = input("Enter Address (optional): ").strip()

    if not name or not phone:
        print("Name and Phone Number are required!")
        return

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    })
    save_contacts(contacts)
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print("-------------------\n")

# Search for a contact
def search_contact():
    query = input("Enter Name or Phone Number to search: ").strip()
    contacts = load_contacts()
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]

    if results:
        print("\n--- Search Results ---")
        for idx, contact in enumerate(results, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
        print("-----------------------\n")
    else:
        print("No contacts found matching your search.")

# Update a contact
def update_contact():
    query = input("Enter Name or Phone Number of the contact to update: ").strip()
    contacts = load_contacts()
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"Updating contact: {contact['name']} - {contact['phone']}")
            contact['name'] = input("Enter New Name: ").strip() or contact['name']
            contact['phone'] = input("Enter New Phone Number: ").strip() or contact['phone']
            contact['email'] = input("Enter New Email (optional): ").strip() or contact['email']
            contact['address'] = input("Enter New Address (optional): ").strip() or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Delete a contact
def delete_contact():
    query = input("Enter Name or Phone Number of the contact to delete: ").strip()
    contacts = load_contacts()
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print(f"Deleting contact: {contact['name']} - {contact['phone']}")
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main menu
def main_menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main_menu()
