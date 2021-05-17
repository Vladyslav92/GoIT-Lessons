import functools


def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return 'Invalid Name!'

    return wrapper


@input_error
def show_all_numbers(data):
    for key, value in data.items():
        print(f'{key}: {value}')


@input_error
def show_number(data, key):
    return data[key]


@input_error
def change_number(data, values):
    if values[1] in data:
        data[values[1]] = values[2]


@input_error
def add_number(data, values):
    data.setdefault(values[1], values[2])


def main():
    base = {}
    stopper = True
    while stopper:
        enter_message = input('message: ')
        if enter_message in ['Hello', 'hello', 'HELLO']:
            print('How can I help you?')
        elif enter_message in ['good bye', 'close', 'exit']:
            print('Good bye!')
            stopper = False
        elif enter_message == 'show all':
            show_all_numbers(base)
        elif enter_message.startswith('phone'):
            key = enter_message.split()
            show_number(base, key[1])
        elif enter_message.startswith('add'):
            key = enter_message.split()
            add_number(base, key)
        elif enter_message.startswith('change'):
            key = enter_message.split()
            change_number(base, key)


if __name__ == '__main__':
    main()
