import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"Contact '{name}' added successfully.")

def search_contact(contacts, query):
    results = []
    for contact in contacts:
        if query.lower() in contact["name"].lower() or query in contact["phone"]:
            results.append(contact)
    
    return results

def delete_contact(contacts, index):
    if 1 <= index <= len(contacts):
        deleted_contact = contacts.pop(index - 1)
        print(f"Contact '{deleted_contact['name']}' deleted successfully.")
    else:
        print("Invalid index. Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book Menu:")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts(contacts)
        elif choice == "2":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
            save_contacts(contacts)
        elif choice == "3":
            query = input("Enter search query: ")
            results = search_contact(contacts, query)
            if results:
                display_contacts(results)
            else:
                print("No matching contacts found.")
        elif choice == "4":
            index = int(input("Enter the index of the contact to delete: "))
            delete_contact(contacts, index)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
