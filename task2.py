"""
This module provides classes for managing an address book.
"""
from collections import UserDict


class Field:
    """
    Represents a generic field.

    Attributes:
        value (str): The value of the field.
    """
    def __init__(self, value):
        """
        Initializes a Field instance.

        Args:
            value (str): The value of the field.
        """
        self.value = value

    def __str__(self):
        """
        Returns a string representation of the field.
        """
        return str(self.value)

class Name(Field):
    """
    Represents a name field.

    Inherits from:
        Field
    """
    def __init__(self, name):
        """
        Initializes a Name instance.

        Args:
            name (str): The name value.
        """
        super().__init__(name)

class Phone(Field):
    """
    Represents a phone number field.

    Inherits from:
        Field
    """
    def __init__(self, phone):
        """
        Initializes a Phone instance.

        Args:
            phone (str): The phone number value.
        """
        super().__init__(phone)
        if len(phone) == 10:
            self.phone = phone
        else:
            print("Not 10 digit number")

class Record:
    """
    Represents a record in the address book.

    Attributes:
        name (Name): The name associated with the record.
        phones (list): List of phone numbers associated with the record.
    """
    def __init__(self, name):
        """
        Initializes a Record instance.

        Args:
            name (str): The name value for the record.
        """
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        """
        Adds a phone number to the record.

        Args:
            phone (str): The phone number to add.
        """
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        """
        Removes a phone number from the record.

        Args:
            phone (str): The phone number to remove.
        """
        phone = Phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        """
        Edits a phone number in the record.

        Args:
            old_phone (str): The old phone number to edit.
            new_phone (str): The new phone number to replace the old one.
        
        Returns:
            str: Message indicating success or failure of the operation.
        """
        old_phone_instance = Phone(old_phone)
        new_phone_instance = Phone(new_phone)
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone_instance.value:
                self.phones[i] = new_phone_instance
                return "Phone successfully changed"
        return "Phone not found"

    def find_phone(self, phone_numb):
        """
        Finds a phone number in the record.

        Args:
            phone_numb (str): The phone number to find.
        
        Returns:
            Phone or str: The phone number object if found, otherwise "Phone not found".
        """
        for phone in self.phones:
            if phone.value == phone_numb:
                return phone
        return "Phone not found"

    def __str__(self):
        """
        Represents an address book.

        Inherits from:
            UserDict
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """
    Represents an address book.

    Inherits from:
        UserDict
    """
    def __init__(self):
        """
        Initializes an AddressBook instance.
        """
        super().__init__()
        self.data = {}

    def add_record(self, record):
        """
        Adds a record to the address book.

        Args:
            record (Record): The record to add.
        """
        self.data[record.name.value] = record

    def find(self, name):
        """
        Finds a record in the address book by name.

        Args:
            name (str): The name to search for.
        
        Returns:
            Record or str: The record if found, otherwise "Not found".
        """
        for record in self.data.values():
            if record.name.value == name:
                return record
        return "Not found"

    def delete(self, name):
        """
        Deletes a record from the address book by name.

        Args:
            name (str): The name of the record to delete.
        
        Returns:
            str: Message indicating success or failure of the operation.
        """
        if name in self.data:
            del self.data[name]
            return "Successfully deleted"
        else:
            return "Unable to delete"
