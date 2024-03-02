from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
   def __init__(self,name):
        super().__init__(name)

class Phone(Field):
   def __init__(self,phone):
        if len(phone) == 10:
            self.phone = phone
        else:
            print("Not 10 digit number")
           

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        self.phones.remove(phone)

    def edit_phone(self, new_phone):
        phone = Phone(new_phone)
        if phone in self.phones:


    def find_phone(self):
        pass
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
   
    def __init__(self):
        super().__init__()
