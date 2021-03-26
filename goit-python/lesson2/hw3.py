
def fibonacci(number):
    if number == 0:
        return 0
    elif len(base) == number:
        return base[number - 1]
    else:
        if len(base) < 2:
            base.append(1)
            base.append(1)
        result = base[-1] + base[-2]
        base.append(result)
        return fibonacci(number)


def main():
    n = int(input("Enter the number: "))
    return fibonacci(n)


if __name__ == '__main__':
    base = []
    print(main())
