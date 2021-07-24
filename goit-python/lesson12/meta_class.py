from abc import ABC, abstractmethod
import json
import pickle


class SerializationInterface(ABC):
    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def to_bin(self):
        pass


class SerializeList(SerializationInterface):
    def to_json(self):
        with open('data_lists.json', 'w') as file:
            json.dump(self, file)

    def to_bin(self):
        with open('data_lists.bin', 'wb') as file:
            pickle.dump(self, file)


class DeserializeList:
    def from_json(self):
        with open('data_lists.json', 'r') as file:
            base = json.load(file)
            return base

    def from_bin(self):
        with open('data_lists.bin', 'rb') as file:
            base = pickle.load(file)
            return base


class SerializeTuple(SerializationInterface):
    def to_json(self):
        with open('data_tuple.json', 'w') as file:
            json.dump(self, file)

    def to_bin(self):
        with open('data_tuple.bin', 'wb') as file:
            pickle.dump(self, file)


class DeserializeTuple:
    def from_json(self):
        with open('data_tuple.json', 'r') as file:
            base = json.load(file)
            return base

    def from_bin(self):
        with open('data_tuple.bin', 'rb') as file:
            base = pickle.load(file)
            return base


class SerializeDict(SerializationInterface):
    def to_json(self):
        with open('data_dicts.json', 'w') as file:
            json.dump(self, file)

    def to_bin(self):
        with open('data_dicts.bin', 'wb') as file:
            pickle.dump(self, file)


class DeserializeDict:
    def from_json(self):
        with open('data_dicts.json', 'r') as file:
            base = json.load(file)
            return base

    def from_bin(self):
        with open('data_dicts.bin', 'rb') as file:
            base = pickle.load(file)
            return base


class SerializeSet(SerializationInterface):
    def to_json(self):
        with open('data_sets.json', 'w') as file:
            json.dump(self, file)

    def to_bin(self):
        with open('data_sets.bin', 'wb') as file:
            pickle.dump(self, file)


class DeserializeSet:
    def from_json(self):
        with open('data_sets.json', 'r') as file:
            base = json.load(file)
            return base

    def from_bin(self):
        with open('data_sets.bin', 'rb') as file:
            base = pickle.load(file)
            return base


class Meta(type):
    children_number = 0

    def __new__(*args):
        Meta.children_number += 1
        print(f'{args}')
        return type.__new__(*args)


class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data

    def class_number(self):
        return Meta.children_number


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data

    def class_number(self):
        return Meta.children_number


try:
    assert (Cls1.class_number, Cls2.class_number) == (0, 1)
    a, b = Cls1(''), Cls2('')
    assert (a.class_number, b.class_number) == (0, 1)
except AssertionError as error:
    print(error)
