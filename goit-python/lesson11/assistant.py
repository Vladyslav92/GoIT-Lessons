from collections import UserDict
from datetime import datetime
import pickle
import re


class AddressBook(UserDict):
    counter = 0

    def __repr__(self):
        return f'{self.data}'

    def add_record(self, record):
        self.data[record] = record

    def iterator(self):
        for i in self.data:
            while self.counter != len(self.data):
                yield i
            self.counter += 1


class Record:
    def __init__(self, name, birthday=None):
        self.name = name
        self.phones = []

    def days_to_birthday(self, data):
        now = datetime.now()
        birthday = datetime(now.year, data.month, data.day)
        return (birthday - now.today()).days + 1

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, phone):
        pass

    def save_information(self):
        base = AddressBook()
        with open('data.bin', 'wb') as fh:
            return pickle.dump(base, fh)

    def show_information(self):
        with open('data.bin', 'rb') as fh:
            return pickle.load(fh)


class Field:
    def find_information(self, any_info):
        base = []
        with open('data.bin', 'rb') as fh:
            base.append(pickle.load(fh))
        for element in base:
            for item in element:
                return re.findall(any_info, item)


class Birthday:
    def __init__(self, birthday):
        self.__phone = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, num):
        try:
            if datetime.strptime(num, "%d.%m.%Y"):
                self.__birthday = num
        except ValueError:
            print('Not correct birth data!')


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if len(phone) >= 10:
            self.__phone = phone
        else:
            print('Not correct phone number!')


name = Name('Vladislav')
phone = Phone('0963455436')
phone_1 = Phone('0956756772')
record_1 = Record(name, '09090909090')
record_1.add_phone(phone)
record_1.add_phone(phone_1)

testing = Birthday('22.08.1992')
print(testing.birthday)

adress = AddressBook()

print(record_1.name.name)
print(record_1.phones[0].phone)
print(record_1.phones[1].phone)
print(adress.iterator)

Record.save_information(record_1)
ss = Record('data.bin')
Record.show_information(ss)
