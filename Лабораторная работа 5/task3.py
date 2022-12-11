import random


def get_unique_list_numbers(start, stop, len_) -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = []
    while len(random_list) != len_:
        number = randint(start, stop)
        if number not in random_list:
            random_list.append(number)
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
