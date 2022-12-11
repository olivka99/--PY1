import random


def get_unique_list_numbers() -> list[int]:
    random_list = [random.randint(-10, 10) for _ in range(15)]  # TODO написать функцию для получения списка уникальных целых чисел
    random_list = list(set(random_list))
    return random_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
