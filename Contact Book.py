class Contact:
  def __init__(self, name, phone_number, email, address):
    self.name = name
    self.phone_number = phone_number
    self.email = email
    self.address = address

  def __str__(self):
    return f"{self.name} - {self.phone_number}"

class ContactBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self):
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    contact = Contact(name, phone_number, email, address)
    self.contacts.append(contact)
    print("Contact added successfully!")

  def view_contacts(self):
    if not self.contacts:
      print("No contacts found.")
      return
    print("**Contact List**")
    for contact in self.contacts:
      print(contact)

  def search_contact(self):
    search_term = input("Enter name or phone number to search: ")
    matches = []
    for contact in self.contacts:
      if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone_number.lower():
        matches.append(contact)
    if matches:
      print("**Search Results**")
      for match in matches:
        print(match)
    else:
      print("No matching contacts found.")

  def update_contact(self):
    name = input("Enter name of contact to update: ")
    for contact in self.contacts:
      if contact.name == name:
        new_name = input("Update name (leave blank to keep): ") or contact.name
        new_phone_number = input("Update phone number (leave blank to keep): ") or contact.phone_number
        new_email = input("Update email (leave blank to keep): ") or contact.email
        new_address = input("Update address (leave blank to keep): ") or contact.address
        contact.name = new_name
        contact.phone_number = new_phone_number
        contact.email = new_email
        contact.address = new_address
        print("Contact updated successfully!")
        return
    print("Contact not found.")

  def delete_contact(self):
    name = input("Enter name of contact to delete: ")
    for i, contact in enumerate(self.contacts):
      if contact.name == name:
        del self.contacts[i]
        print("Contact deleted successfully!")
        return
    print("Contact not found.")

def main():
  contact_book = ContactBook()
  while True:
    print("\n**Contact Book Menu**")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
      contact_book.add_contact()
    elif choice == "2":
      contact_book.view_contacts()
    elif choice == "3":
      contact_book.search_contact()
    elif choice == "4":
      contact_book.update_contact()
    elif choice == "5":
      contact_book.delete_contact()
    elif choice == "6":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
