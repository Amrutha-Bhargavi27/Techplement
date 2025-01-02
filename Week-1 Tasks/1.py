import json
import re

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Helper function to load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}
    return contacts

# Helper function to save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Validate phone number format
def validate_phone(phone):
    return re.match(r"^\+?1?\d{9,15}$", phone) is not None

# Validate email format
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone (+1234567890): ")
    email = input("Enter contact email: ")
    
    # Validate phone number and email
    if not validate_phone(phone):
        print("Invalid phone number format. Try again.")
        return
    if not validate_email(email):
        print("Invalid email format. Try again.")
        return
    
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact for {name} added successfully!")

# Function to search for a contact by name
def search_contact(contacts):
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print(f"Contact for {name} not found.")

# Function to update a contact's information
def update_contact(contacts):
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number for {name} (+1234567890): ")
        email = input(f"Enter new email for {name}: ")

        if validate_phone(phone) and validate_email(email):
            contacts[name] = {"phone": phone, "email": email}
            save_contacts(contacts)
            print(f"Contact for {name} updated successfully!")
        else:
            print("Invalid phone or email format. Contact not updated.")
    else:
        print(f"Contact for {name} not found.")

# Main function to handle user input
def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()