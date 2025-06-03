
class Contact:
    """A class representing a contact with name, phone, and email."""
    def __init__(self, name, phone, email):
        """Initialize contact with name, phone, and email."""
        self._name = name
        self._phone = phone
        self._email = email
    
    @property
    def name(self):
        """Get the contact's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the contact's name, ensuring it's not empty."""
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()
    
    @property
    def phone(self):
        """Get the contact's phone number."""
        return self._phone
    
    @phone.setter
    def phone(self, value):
        """Set the phone number, ensuring it's valid."""
        if not self._is_valid_phone(value):
            raise ValueError("Invalid phone number")
        self._phone = value
    
    @property
    def email(self):
        """Get the contact's email."""
        return self._email
    
    @email.setter
    def email(self, value):
        """Set the email, ensuring it's valid."""
        if not self._is_valid_email(value):
            raise ValueError("Invalid email address")
        self._email = value
    
    @staticmethod
    def _is_valid_phone(phone):
        """Check of phone number is valid (simple check: digits and optional +,-,spaces)"""
        cleaned = ''.join(c for c in phone if c.isdigit() or c in ['+', '-', ' '])
        return len(cleaned) >= 7  # Basic validation
    
    @staticmethod
    def _is_valid_email(email):
        """Check if email is valid (contains @ and .)."""
        return '@' in email and '.' in email and len(email) > 5
    
    def __str__(self):
        """Return string representation of the contact."""
        return f"Name: {self._name}, Phone: {self._phone}, Email: {self._email}"
    
class ContactBook:
    """Return string representation of the contact."""
    def __init__(self):
        """Initialize an empty contact book."""
        self._contacts = {}

    def add_contact(self, name, phone, email):
        """Add a new contact to the book."""
        if name in self._contacts:
            raise ValueError(f"Contact '{name}' already exists")
        contact = Contact(name, phone, email)
        self._contacts[name] = contact
        return contact
    
    def update_contact(self, name, phone=None, email=None):
        """Update an existing contact's phone and/or email."""
        if name not in self._contacts:
            raise ValueError(f"Contact '{name}' not found")
        contact = self._contacts[name]
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        return contact
    
    def delete_contact(self, name):
        """Delete a contact by name."""
        if name not in self._contacts:
            raise ValueError(f"Contact '{name}' not found")
        return self._contacts.pop(name)
    
    def search_contact(self, name):
        """Search for a contact by name."""
        return self._contacts.get(name)
    
    def list_contacts(self):
        """Return a list of all contacts."""
        return list(self._contacts.values())
    
    def __len__(self):
        """Return the number of contacts."""
        return len(self._contacts)
    
def main():
    """Main function to demonstrate the Contact Book functionality."""
    book = ContactBook()
    try:
        # Add contacts
        book.add_contact("Alice Smith", "+1234567890", "alice@example.com")
        book.add_contact("Bob Jones", "987-654-3210", "bob@example.com")
        print("\nAll contacts:")
        for contact in book.list_contacts():
            print(contact)
        
        # Search for a contact
        print("\nSearching for Alice:")
        contact = book.search_contact("Alice Smith")
        print(contact if contact else "Not found")
        
        # Update a contact
        print("\nUpdating Bob's email:")
        book.update_contact("Bob Jones", email="bob.new@example.com")
        print(book.search_contact("Bob Jones"))
        
        # Delete a contact
        print("\nDeleting Alice:")
        book.delete_contact("Alice Smith")
        print(f"Number of contacts: {len(book)}")
        
        # Try adding an invalid contact
        print("\nTrying to add an invalid contact:")
        book.add_contact("Charlie", "123", "invalid")  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()