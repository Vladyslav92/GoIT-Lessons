from collections import UserDict
from datetime import datetime


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


class Field:
    pass


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
