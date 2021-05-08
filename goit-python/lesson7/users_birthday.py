import datetime

users = [
    {'name': 'Vladislav', 'birthday': datetime.date(2021, 5, 10)},
    {'name': 'Anna', 'birthday': datetime.date(2021, 5, 12)},
    {'name': 'Andrey', 'birthday': datetime.date(2021, 5, 14)},
    {'name': 'Kristina', 'birthday': datetime.date(2021, 5, 16)},
    {'name': 'Katya', 'birthday': datetime.date(2021, 5, 11)},
    {'name': 'Natasha', 'birthday': datetime.date(2021, 5, 13)},
    {'name': 'Alexandr', 'birthday': datetime.date(2021, 5, 15)},
    {'name': 'Karolina', 'birthday': datetime.date(2021, 5, 13)}
]


def congratulate(users_list):
    base = [['Monday: '], ['Tuesday: '], ['Wednesday: '], ['Thursday: '], ['Friday: ']]
    for dicts in users_list:
        if dicts['birthday'].timetuple().tm_wday == 0 or \
                dicts['birthday'].timetuple().tm_wday == 5 or dicts['birthday'].timetuple().tm_wday == 6:
            base[0].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 1:
            base[1].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 2:
            base[2].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 3:
            base[3].append(dicts['name'])
        elif dicts['birthday'].timetuple().tm_wday == 4:
            base[4].append(dicts['name'])
    for element in base:
        if len(element) > 1:
            element = ', '.join(element).replace(',', '', 1)
            print(element)


congratulate(users)
