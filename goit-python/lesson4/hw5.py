enter_string = input("Enter your string: ")


def normalize(string):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for x in string:
        if x in alphabet:
            string = string.replace(x, '_')
    return string


print(normalize(enter_string))
