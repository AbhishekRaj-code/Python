# Creating class Contact to manage phone book entries
# Each contact will have a name, phone number, and optional email
# The class will also maintain a directory of all contacts
# Methods will include adding, searching, displaying, and deleting contacts
# Additionally, input validation methods will ensure correct formats for phone numbers and emails
# The phone number should only contain digits and dashes, and the email should follow a basic email pattern
# The program will provide a simple text-based menu for user interaction


import re
class Contact:
    # Class variable to hold all contacts
    phone_directory = []

    # Constructor to initialize contact details
    def __init__(self, name, phone_number, email=None):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        # Add the new contact to the phone directory
        Contact.phone_directory.append(self)

    # Method to display contact information
    def display_contact(self, ):
        contact_info = f"Name: {self.name}, Phone Number: {self.phone_number}, Email: {self.email}"
        #if self.email:
        #    contact_info += f", Email: {self.email}"
        return contact_info
    
    # Class method to display all contacts in the phone directory
    @classmethod
    def display_all_contacts(cls):
        # Check if the phone directory is empty
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory")
        # If not empty, display each contact's information
        else:
            for contact in cls.phone_directory:
                print(contact.display_contact())

    # Class method to search for a contact by name
    @classmethod
    def search_contact(cls, search_name):
        # Iterate through the phone directory to find the contact
        for contact in cls.phone_directory:
            if contact.name.lower() == search_name.lower():
                return contact.name + ": " + contact.phone_number + (f", Email: {contact.email}")
        return f"Contact not found for {search_name}"
    

    # Class method to delete a contact by name
    @classmethod
    def delete_contact(cls, delete_name):
        # Iterate through the phone directory to find and delete the contact
        for contact in cls.phone_directory:
            if contact.name.lower() == delete_name.lower():
                cls.phone_directory.remove(contact)
                return f"Contact {delete_name} deleted successfully."
        return f"Contact not found for {delete_name}"
    

    # Static method to validate phone number format
    @staticmethod
    def validate_phone_number(phone_number):
        # Simple validation: check if the phone number contains only digits and dashes
        
        pattern = re.compile(r'^[\d-]+$')
        # Ensure phone number length is between 10 and 12 characters
        if len(phone_number) < 10 or len(phone_number) > 12:
            return False
        else:
            return bool(pattern.match(phone_number))
    
    # Static method to validate email format
    @staticmethod
    def validate_email(email):
        # Simple validation: check if the email follows a basic pattern
        pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        return bool(pattern.match(email))
    
    @staticmethod
    def validate_name(name):
        # Check if the contact name already exists in the phone directory
        for contact in Contact.phone_directory:
            if contact.name.lower() == name.lower():
                return False
        return True

# Main program loop for user interaction   
while True:
    print("Phone Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    # Get user choice
    choice = input("Enter your choice (1-5): ")

    # Handle user choices
    if choice == '5':
        print("Exiting Phone Book. Goodbye!")
        break
    # Add Contact
    elif choice == '1':
        n_contacts = int(input("Enter number of contacts to add: "))
        # Loop to add multiple contacts
        for i in range(n_contacts):
            name = input("Enter contact name: ")
            while not Contact.validate_name(name):
                print("Contact a;ready exists. Please enter a different name.")
                name = input("Enter contact name: ")
            phone_number = input("Enter phone number (digits and dashes only): ")
            # Validate phone number format
            while not Contact.validate_phone_number(phone_number):
                print("Invalid phone number format. Please enter again.")
                phone_number = input("Enter phone number (digits and dashes only): ")
            email = input("Enter email address (optional, press enter to skip): ")
            # Validate email format if provided
            if email:
                while not Contact.validate_email(email):
                    print("Invalid email format. Please enter again.")
                    email = input("Enter email address (optional, press enter to skip): ")
            else:
                email = None
            # Create a new contact
            Contact(name, phone_number, email)

    # Search Contact
    elif choice == '2':
        search_name = input("Enter the name of the contact to search: ")
        result = Contact.search_contact(search_name)
        print(result)
    
    # Display All Contacts
    elif choice == '3':
        Contact.display_all_contacts()

    # Delete Contact
    elif choice == '4':
        delete_name = input("Enter the name of the contact to delete: ")
        result = Contact.delete_contact(delete_name)
        print(result)
    
    # Invalid Choice
    else:
        print("Invalid choice. Please select a valid option (1-5).")

