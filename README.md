Contact Book Application by Qistina.
Overview
This is a simple command-line Contact Book application written in Python. It allows users to manage a collection of contacts, with functionality to add, update, delete, search, and list contacts. Each contact includes a name, phone number, and email address, with basic validation for phone numbers and email addresses.
Features

Add Contact: Create a new contact with a name, phone number, and email address.
Update Contact: Modify an existing contact's phone number and/or email address.
Delete Contact: Remove a contact by name.
Search Contact: Find a contact by name.
List Contacts: Display all contacts in the book.
Input Validation: Ensures phone numbers and email addresses meet basic format requirements.

Requirements

Python 3.x

Installation

Clone or download the project files.
Ensure Python 3 is installed on your system.
Place the miniproject.py file in your working directory.

Usage

Run the program using the command:python miniproject.py


The main() function includes a demonstration of the Contact Book's functionality, including:
Adding sample contacts
Listing all contacts
Searching for a contact
Updating a contact's email
Deleting a contact
Attempting to add an invalid contact (to demonstrate error handling)



Code Structure

Contact Class:
Stores individual contact details (name, phone, email).
Includes property decorators for validation and access control.
Validates phone numbers (minimum 7 digits, allows +, -, and spaces) and email addresses (must contain @ and .).


ContactBook Class:
Manages a collection of contacts stored in a dictionary.
Provides methods to add, update, delete, search, and list contacts.


Main Function:
Demonstrates the usage of the ContactBook and Contact classes with example operations.



Example Output
When you run miniproject.py, you will see output similar to the following:
All contacts:
Name: Alice Smith, Phone: +1234567890, Email: alice@example.com
Name: Bob Jones, Phone: 987-654-3210, Email: bob@example.com

Searching for Alice:
Name: Alice Smith, Phone: +1234567890, Email: alice@example.com

Updating Bob's email:
Name: Bob Jones, Phone: 987-654-3210, Email: bob.new@example.com

Deleting Alice:
Number of contacts: 1

Trying to add an invalid contact:
Error: Invalid phone number

Limitations

Phone number validation is basic (checks for minimum length and allowed characters).
Email validation is minimal (checks for presence of @ and .).
The application runs in the console and does not persist data between sessions.
No graphical user interface is provided.

Future Improvements

Add persistent storage (e.g., save contacts to a file or database).
Implement more robust phone and email validation (e.g., regex-based).
Add a user interface (e.g., CLI with interactive prompts or a GUI).
Allow batch

