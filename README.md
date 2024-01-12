
# PhoneBook - Simple Python Phone Book using Hash Tables

## Overview

This repository contains a simple implementation of a phone book in Python using hash tables. The project consists of classes for `PhoneRecord`, `HashTableRecord`, and `PhoneBook`, offering basic functionalities such as adding, deleting, and fetching contacts.

## Features

- **Add Contacts:** Add new contacts to the phone book with name, organization, and phone numbers.
- **Delete Contacts:** Remove contacts based on their name.
- **Fetch Contacts:** Retrieve contacts matching a query from the phone book.
- **Read from CSV:** Populate the phone book by reading records from a CSV file.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/phone-book.git
    cd phone-book
    ```

2. Run the example script or integrate the `PhoneBook` class into your project.

    ```bash
    python example.py
    ```

## Usage

1. Create a `PhoneBook` instance:

    ```python
    phone_book = PhoneBook()
    ```

2. Add contacts:

    ```python
    contact_info = "John Doe, Organization Inc., 1234567890"
    phone_record = phone_book.create_phone_record(contact_info)
    phone_book.add_contact(phone_record)
    ```

3. Delete contacts:

    ```python
    phone_book.delete_contact("John Doe")
    ```

4. Fetch contacts:

    ```python
    results = phone_book.fetch_contacts("John")
    print("Matching Contacts:", results)
    ```

5. Read records from a CSV file:

    ```python
    phone_book.read_records_from_file("contacts.csv")
    ```



