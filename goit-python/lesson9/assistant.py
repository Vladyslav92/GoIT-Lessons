from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record] = record


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone):
        pass


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


name = Name('Vladislav')
phone = Phone('0963455436')
phone_1 = Phone('0956756772')
record_1 = Record(name)
record_1.add_phone(phone)
record_1.add_phone(phone_1)

print(record_1.name.name)
print(record_1.phones[0].phone)
print(record_1.phones[1].phone)
